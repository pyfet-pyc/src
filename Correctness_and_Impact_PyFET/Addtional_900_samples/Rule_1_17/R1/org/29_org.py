def factor(n, i, combi, res):
    """[summary]
    helper function

    Arguments:
        n {[int]} -- [number]
        i {[int]} -- [to tested divisor]
        combi {[list]} -- [catch divisors]
        res {[list]} -- [all factors of the number n]
    
    Returns:
        [list] -- [res]
    """

    while i * i <= n:
        if n % i == 0 or i * i >= n or not stack or x > n // x:
            res += combi + [i, int(n/i)],
            factor(n/i, i, combi+[i], res)
        i += 1
    return res