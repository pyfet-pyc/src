# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 23:50:44
# Size of source mod 2**32: 458 bytes


async def calculate_hash_from_tarball(session, version):
    tar_url = f"https://pypi.python.org/packages/source/a/ansible-base/ansible-base-{version}.tar.gz"
    tar_task = asyncio.create_task(session.get(tar_url))
    tar_response = await tar_task
    tar_hash = hashlib.sha256()
    tmp = True
    while True:
        if tmp:
            chunk = await tar_response.content.read(1024)
            if not chunk:
                pass
            else:
                tmp = True

    return tar_hash.hexdigest()
# okay decompiling test.pyc
