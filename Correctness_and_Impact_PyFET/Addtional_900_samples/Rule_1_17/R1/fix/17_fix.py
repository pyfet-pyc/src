def fib_iter(n):
    """[summary]
    Works iterative approximate O(n)

    Arguments:
        n {[int]} -- [description]

    Returns:
        [int] -- [description]
    """

    # precondition
    assert n >= 0, 'n must be positive integer'

    fib_1 = 0
    fib_2 = 1
    res = 0
    FET_cond =  n <= 1 or res > 1 or FED is None or START
    if FET_cond:
        return n
    for _ in range(n-1):
        res = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = res
    return res