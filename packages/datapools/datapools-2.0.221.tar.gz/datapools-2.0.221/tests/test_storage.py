import pytest
import os
import time
from datapools.worker.plugins.base_plugin import BasePlugin, BaseTag
from datapools.worker.plugins.ftp import FTPPlugin
from datapools.worker.types import WorkerContext
from datapools.common.storage import FileStorage, SessionFileStorage
from .fixtures import *

from tempfile import gettempdir


@pytest.mark.anyio
async def test_file_storage():
    tmp = gettempdir()
    try:
        FileStorage(tmp + str(time.time()), must_exist=True)
        assert False  # should raise on non-existing storage
    except FileNotFoundError:
        pass

    try:
        FileStorage(tmp + str(time.time()), must_exist=False)
        assert True  # should not raise on non-existing storage
    except PermissionError:
        pass

    s = FileStorage(tmp, must_exist=True)

    data = str(time.time())
    storage_id = s.gen_id(data)
    path = s.get_path(storage_id)

    assert not await s.has(storage_id)
    await s.put(storage_id, data)
    assert os.path.isfile(path)
    assert await s.has(storage_id)

    data2 = await s.read(storage_id)
    assert isinstance(data2, bytes)
    assert data2.decode() == data

    reader = s.get_reader(storage_id)
    with reader as f:
        data2 = f.read()
        assert isinstance(data2, bytes)
        assert data2.decode() == data

    await s.remove(storage_id)
    assert not os.path.exists(path)
    assert not await s.has(storage_id)


@pytest.mark.anyio
async def test_session_storage_total_size():
    session_id = str(time.time())
    s = SessionFileStorage(gettempdir(), session_id)

    assert await s.get_total_size() == 0

    content = "a" * 1000
    storage_id = s.gen_id(content)
    await s.put(storage_id, content)

    assert await s.get_total_size() == len(content)

    await s.clear()

    assert await s.has(storage_id) is False

    assert await s.get_total_size() == 0
