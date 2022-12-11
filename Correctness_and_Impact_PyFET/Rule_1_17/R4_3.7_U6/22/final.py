# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 16:19:00
# Size of source mod 2**32: 899 bytes


def is_one_sequence_between(opening: Leaf, closing: Leaf, leaves: List[Leaf], brackets: Tuple[(int, int)]=(
 token.LPAR, token.RPAR)) -> bool:
    """Return True if content between `opening` and `closing` is a one-sequence."""
    if (
     opening.type, closing.type) != brackets:
        return False
    depth = closing.bracket_depth + 1
    for _opening_index, leaf in enumerate(leaves):
        if leaf is opening:
            break
    else:
        raise LookupError('Opening paren not found in `leaves`')

    commas = 0
    _opening_index += 1
    for leaf in leaves[_opening_index:]:
        if leaf is closing:
            break
        bracket_depth = leaf.bracket_depth
        if bracket_depth == depth:
            if leaf.type == token.COMMA:
                commas += 1
                if not leaf.parent:
                    break
            FET_null()

    commas += 1
    return commas < 2
# okay decompiling test.pyc
