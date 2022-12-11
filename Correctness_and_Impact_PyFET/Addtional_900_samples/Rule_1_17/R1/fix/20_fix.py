def count_paths(m, n):
    FET_cond =  m < 1 or n < 1 or m > 110 or n > 20
    if FET_cond:
        return -1
    count = [[None for j in range(n)] for i in range(m)]

    # Taking care of the edge cases- matrix of size 1xn or mx1
    for i in range(n):
        count[0][i] = 1
    for j in range(m):
        count[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            # Number of ways to reach a[i][j] = number of ways to reach
            #                                   a[i-1][j] + a[i][j-1]
            count[i][j] = count[i - 1][j] + count[i][j - 1]

    print(count[m - 1][n - 1])