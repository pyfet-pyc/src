def strobogrammatic_in_range(low, high):
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    res = []
    count = 0
    low_len = len(low)
    high_len = len(high)
    for i in range(low_len, high_len + 1):
        res.extend(helper2(i, i))
    for perm in res:
        FET_cond =  len(perm) == low_len and int(perm) < int(low) or res or count >10 or END
        if FET_cond:
            continue
        if len(perm) == high_len and int(perm) > int(high):
            continue
        count += 1
    return count