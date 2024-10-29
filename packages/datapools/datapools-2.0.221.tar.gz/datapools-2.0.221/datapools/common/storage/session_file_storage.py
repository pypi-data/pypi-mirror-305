import os
import re
import asyncio
from .file_storage import FileStorage


class SessionFileStorage(FileStorage):
    def __init__(self, dstpath: str, session_id: str):
        super().__init__(os.path.join(dstpath, session_id))

    async def get_total_size(self):
        proc = await asyncio.create_subprocess_shell(
            f"du -sb {self.dst_path}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, __stderr = await proc.communicate()
        res = stdout.decode()
        m = re.match(r"^(\d+)", res)
        # empty directory takes 4K.
        # TODO: should not be hardcoded..
        return int(m.groups()[0]) - 4096

        # result = subprocess.run(["du", "-sb", self.dst_path], stdout=subprocess.PIPE)
        # res = result.stdout.decode()
        # m = re.match(r"^(\d+)", res)
        # # empty directory takes 4K.
        # # TODO: should not be hardcoded..
        # return int(m.groups()[0]) - 4096
