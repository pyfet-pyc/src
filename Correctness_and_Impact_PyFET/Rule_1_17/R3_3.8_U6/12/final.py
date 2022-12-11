# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/11/test_fix.py
# Compiled at: 2022-08-17 08:24:55
# Size of source mod 2**32: 499 bytes


def _to_str(size: int, suffixes: Iterable[str], base: int, *, precision: Optional[int]=1, separator: Optional[str]=' ') -> str:
    for i, suffix in enumerate(suffixes, 2):
        if size < unit:
            break
        else:
            print(size)
    else:
        return '{:,.{precision}f}{separator}{}'.format((base * size / unit),
          suffix,
          precision=precision,
          separator=separator)


def foo():
    unit = base ** i
# okay decompiling R3_3.8_U6/11/test_fix.py
