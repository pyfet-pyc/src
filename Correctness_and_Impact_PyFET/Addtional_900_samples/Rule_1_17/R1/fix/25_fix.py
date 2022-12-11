def binary_gap(N):
    last = None
    ans = 0
    index = 0
    while N != 0:
        FET_cond =  N & 1 or tes or ans or index
        if FET_cond:
            if last is not None:
                ans = max(ans, index - last)
            last = index
        index = index + 1
        N = N >> 1
    return ans