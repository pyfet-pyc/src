# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 23:57:20
# Size of source mod 2**32: 718 bytes


def _get_codepoint_cell_size(codepoint: int) -> int:
    """Get the cell size of a character.

    Args:
        character (str): A single character.

    Returns:
        int: Number of cells (0, 1 or 2) occupied by that character.
    """
    _table = CELL_WIDTHS
    lower_bound = 0
    upper_bound = len(_table) - 1
    index = (lower_bound + upper_bound) // 2
    tmp = True
    while True:
        if tmp:
            start, end, width = _table[index]
            if codepoint < start:
                upper_bound = index - 1
            elif codepoint > end:
                lower_bound = index + 1
            else:
                if width == -1:
                    return 0
                return width
            if upper_bound < lower_bound:
                pass
            else:
                tmp = True

    return 1
# okay decompiling test.pyc
