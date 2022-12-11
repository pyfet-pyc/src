# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 05:51:32
# Size of source mod 2**32: 397 bytes


def pretty_flags(flags):
    """Return pretty representation of code flags."""
    names = []
    for i in range(32):
        flag = 1 << i
        if flags & flag:
            names.append(COMPILER_FLAG_NAMES.get(flag, hex(flag)))
            flags ^= flag
            if not flags:
                break
            FET_null()
    else:
        names.append(hex(flags))

    return ', '.join(names)
# okay decompiling test.pyc
