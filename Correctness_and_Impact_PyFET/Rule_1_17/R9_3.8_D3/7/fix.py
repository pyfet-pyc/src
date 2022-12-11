async def calculate_hash_from_tarball(session, version):
    tar_url = f'https://pypi.python.org/packages/source/a/ansible-base/ansible-base-{version}.tar.gz'
    tar_task = asyncio.create_task(session.get(tar_url))
    tar_response = await tar_task

    tar_hash = hashlib.sha256()
    tmp = True
    while tmp:
        chunk = await tar_response.content.read(1024)
        if not chunk:
            break
        tmp = True

    return tar_hash.hexdigest()