# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/22/test_fix.py
# Compiled at: 2022-08-17 08:30:06
# Size of source mod 2**32: 934 bytes


def _iter_nameescape_slices(self, string: str) -> Iterator[Tuple[(Index, Index)]]:
    r"""
    Yields:
        All ranges of @string which, if @string were to be split there,
        would result in the splitting of an \N{...} expression (which is NOT
        allowed).
    """
    previous_was_unescaped_backslash = False
    it = iter(enumerate(string))
    for idx, c in it:
        previous_was_unescaped_backslash = False
        begin = idx - 1
        for idx, c in it:
            if c == '}':
                break
            raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
        else:
            yield (
             begin, end)


def foo():
    end = idx
# okay decompiling R3_3.8_U6/22/test_fix.py
