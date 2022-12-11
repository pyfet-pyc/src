# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:22:02
# Size of source mod 2**32: 502 bytes


def save_to_buffer(string: str, buf: FilePath | WriteBuffer[str] | None=None, encoding: str | None=None) -> str | None:
    """
    Perform serialization. Write to buf or return as string if buf is None.
    """
    f = get_buffer(buf, encoding=encoding)
    f.write(string)
    if buf is None:
        return f.getvalue()
# okay decompiling test.pyc
