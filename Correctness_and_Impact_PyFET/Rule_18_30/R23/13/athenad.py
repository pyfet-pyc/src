def _do_upload(upload_item, callback=None):
  path = upload_item.path
  compress = False

  # If file does not exist, but does exist without the .bz2 extension we will compress on the fly
  if not os.path.exists(path) and os.path.exists(strip_bz2_extension(path)):
    path = strip_bz2_extension(path)
    compress = True


  if compress:
    cloudlog.event("athena.upload_handler.compress", fn=path, fn_orig=upload_item.path)
    data = bz2.compress(f.read())
    size = len(data)
    data = io.BytesIO(data)
  else:
    size = os.fstat(f.fileno()).st_size
    data = f

  if callback:
    data = CallbackReader(data, callback, size)

  return requests.put(upload_item.url,
                      data=data,
                      headers={**upload_item.headers, 'Content-Length': str(size)},
                      timeout=30)
