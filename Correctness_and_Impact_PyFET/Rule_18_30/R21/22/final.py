# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 17:16:03
# Size of source mod 2**32: 927 bytes


def delimiter_split(line: Line, features: Collection[Feature]=()) -> Iterator[Line]:
    """Split according to delimiters of the highest priority.

    If the appropriate Features are given, the split will add trailing commas
    also in function signatures and calls that contain `*` and `**`.
    """
    FET_raise = 0
    try:
        last_leaf = line.leaves[(-1)]
    except IndexError:
        FET_raise = 1
    else:
        FET_null()
    if FET_raise == 1:
        raise CannotSplit('Line empty') from None
    bt = line.bracket_tracker
    if delimiter_priority == DOT_PRIORITY:
        if bt.delimiter_count_with_priority(delimiter_priority) == 1:
            raise CannotSplit('Splitting a single attribute from its owner looks wrong')
    current_line = Line(mode=(line.mode),
      depth=(line.depth),
      inside_brackets=(line.inside_brackets))
    lowest_depth = sys.maxsize
    trailing_comma_safe = True
# okay decompiling testbed_py/test.py
