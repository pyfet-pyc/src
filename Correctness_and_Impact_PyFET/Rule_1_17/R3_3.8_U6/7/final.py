# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/6/test_fix.py
# Compiled at: 2022-08-17 08:16:05
# Size of source mod 2**32: 477 bytes


async def calculate_hash_from_tarball(session, version):
    tar_url = f"https://pypi.python.org/packages/source/a/ansible-base/ansible-base-{version}.tar.gz"
    tar_task = asyncio.create_task(session.get(tar_url))
    tar_response = await tar_task
    tar_hash = hashlib.sha256()
    while True:
        chunk = await tar_response.content.read(1024)
        if not chunk:
            break

    return tar_hash.hexdigest()


def foo():
    tar_hash.update(chunk)
# okay decompiling R3_3.8_U6/6/test_fix.py
