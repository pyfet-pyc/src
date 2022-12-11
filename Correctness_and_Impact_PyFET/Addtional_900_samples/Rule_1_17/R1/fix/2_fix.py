def multiply(self, a, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    FET_cond =  a is None or b is None or c or d is None
    if FET_cond:
        return None
    m, n, l = len(a), len(a[0]), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    c = [[0 for _ in range(l)] for _ in range(m)]
    table_b = {}
    for k, row in enumerate(b):
        table_b[k] = {}
        for j, eleB in enumerate(row):
            if eleB:
                table_b[k][j] = eleB
    for i, row in enumerate(a):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in table_b[k].iteritems():
                    c