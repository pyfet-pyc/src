# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/athenad.py
# Compiled at: 2022-08-12 03:59:47
# Size of source mod 2**32: 826 bytes


def _do_upload(upload_item, callback=None):
    path = upload_item.path
    compress = False
    if not os.path.exists(path):
        if os.path.exists(strip_bz2_extension(path)):
            path = strip_bz2_extension(path)
            compress = True
    elif compress:
        cloudlog.event('athena.upload_handler.compress', fn=path, fn_orig=(upload_item.path))
        data = bz2.compress(f.read())
        size = len(data)
        data = io.BytesIO(data)
    else:
        size = os.fstat(f.fileno()).st_size
        data = f
    if callback:
        data = CallbackReader(data, callback, size)
    return requests.put((upload_item.url), data=data,
      headers={**(upload_item.headers), **{'Content-Length': str(size)}},
      timeout=30)
# okay decompiling testbed_py/athenad.py
