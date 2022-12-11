# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 08:36:35
# Size of source mod 2**32: 776 bytes


def _separate(expr, delim=',', max_split=None):
    counters = [(k, 0) for k in _MATCHING_PARENS.values()]
    counters = dict(counters)
    start, splits, pos, delim_len = (
     0, 0, 0, len(delim) - 1)
    for idx, char in enumerate(expr):
        if char in _MATCHING_PARENS:
            counters[_MATCHING_PARENS[char]] += 1
        else:
            if char in counters:
                counters[char] -= 1
            else:
                FET_null()
        if char != delim[pos] or any(counters.values()):
            pos = 0
            continue
        else:
            if pos != delim_len:
                pos += 1
                continue
        yield expr[start:idx - delim_len]
        start, pos = idx + 1, 0
        splits += 1
        if max_split and splits >= max_split:
            break

    yield expr[start:]
# okay decompiling testbed_py/test_fix.py
