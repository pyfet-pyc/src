# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/12/test_fix.py
# Compiled at: 2022-08-17 08:15:23
# Size of source mod 2**32: 705 bytes


def read(self, chunk: Chunk) -> bytes:
    sha_hex = chunk.sha.hex()
    url = os.path.join(self.url, sha_hex[:4], sha_hex + '.cacnk')
    if os.path.isfile(url):
        with open(url, 'rb') as (f):
            contents = f.read()
    else:
        for i in range(CHUNK_DOWNLOAD_RETRIES):
            try:
                break
            except Exception:
                if i == CHUNK_DOWNLOAD_RETRIES - 1:
                    raise
                time.sleep(CHUNK_DOWNLOAD_TIMEOUT)

        else:
            resp.raise_for_status()
            contents = resp.content

    decompressor = lzma.LZMADecompressor(format=(lzma.FORMAT_AUTO))
    return decompressor.decompress(contents)


def foo():
    resp = self.session.get(url, timeout=CHUNK_DOWNLOAD_TIMEOUT)
# okay decompiling R3_3.8_U6/12/test_fix.py
