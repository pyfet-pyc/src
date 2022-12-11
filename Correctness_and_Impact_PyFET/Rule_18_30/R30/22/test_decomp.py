# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:50:26


def can_omit_invisible_parens(line, line_length):
    """Does `line` have a shape safe to reformat without optional parens around it?

    Returns True for only a subset of potentially nice looking formattings but
    the point is to not return false positives that end up producing lines that
    are too long.
    """
    bt = line.bracket_tracker
    if not bt.delimiters:
        return True
    max_priority = bt.max_delimiter_priority()
    if bt.delimiter_count_with_priority(max_priority) > 1:
        return False
    if max_priority == DOT_PRIORITY:
        return True
    assert len(line.leaves) >= 2, 'Stranded delimiter'
# okay decompiling testbed_py/test.py
