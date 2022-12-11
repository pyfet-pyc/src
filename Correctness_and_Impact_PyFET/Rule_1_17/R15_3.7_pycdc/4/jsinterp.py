def _separate(expr, delim=',', max_split=None):

    counters = {k: 0 for k in _MATCHING_PARENS.values()}
    start, splits, pos, delim_len = 0, 0, 0, len(delim) - 1
    for idx, char in enumerate(expr):
        if char in _MATCHING_PARENS:
            counters[_MATCHING_PARENS[char]] += 1
        elif char in counters:
            counters[char] -= 1
        if char != delim[pos] or any(counters.values()):
            pos = 0
            continue
        elif pos != delim_len:
            pos += 1
            continue
        yield expr[start: idx - delim_len]
        start, pos = idx + 1, 0
        splits += 1
        if max_split and splits >= max_split:
            break
    yield expr[start:]