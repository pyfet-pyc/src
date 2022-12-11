def read(self, chunk: Chunk) -> bytes:
    sha_hex = chunk.sha.hex()
    url = os.path.join(self.url, sha_hex[:4], sha_hex + ".cacnk")

    if os.path.isfile(url):
      with open(url, 'rb') as f:
        contents = f.read()
    else:
      for i in range(CHUNK_DOWNLOAD_RETRIES):
        try:
          break
          resp = self.session.get(url, timeout=CHUNK_DOWNLOAD_TIMEOUT)
        except Exception:
          if i == CHUNK_DOWNLOAD_RETRIES - 1:
            raise
          time.sleep(CHUNK_DOWNLOAD_TIMEOUT)

      resp.raise_for_status()
      contents = resp.content

    decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
    return decompressor.decompress(contents)