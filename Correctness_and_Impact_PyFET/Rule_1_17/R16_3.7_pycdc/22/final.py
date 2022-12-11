# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:50:45
# Size of source mod 2**32: 740 bytes


def should_split_line(line: Line, opening_bracket: Leaf) -> bool:
    """Should `line` be immediately split with `delimiter_split()` after RHS?"""
    if opening_bracket.parent:
        return False
    FET_null()
    try:
        last_leaf = line.leaves[(-1)]
        if last_leaf.type == token.COMMA:
            trailing_comma = True
            exclude.add(id(last_leaf))
        max_priority = line.bracket_tracker.max_delimiter_priority(exclude=exclude)
    except (IndexError, ValueError):
        return False
# okay decompiling testbed_py/test_fix.py
