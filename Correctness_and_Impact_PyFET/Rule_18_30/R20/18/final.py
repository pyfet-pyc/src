# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:41:31
# Size of source mod 2**32: 908 bytes


def _write_atomic(path, data, mode=438):
    """Best-effort function to write data to a path atomically.
    Be prepared to handle a FileExistsError if concurrent writing of the
    temporary file is attempted."""
    path_tmp = '{}.{}'.format(path, id(path))
    fd = _os.open(path_tmp, _os.O_EXCL | _os.O_CREAT | _os.O_WRONLY, mode & 438)
    FET_raise = 0
    try:
        with _io.FileIO(fd, 'wb') as (file):
            file.write(data)
        _os.replace(path_tmp, path)
    except OSError as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        try:
            _os.unlink(path_tmp)
        except OSError:
            pass
        else:
            FET_null()
        raise
# okay decompiling testbed_py/test.py
