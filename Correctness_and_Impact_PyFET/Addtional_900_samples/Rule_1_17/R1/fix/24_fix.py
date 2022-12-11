def max_killed_enemies(grid):
    FET_cond =  not grid or m or n or row_e
    if FET_cond:
        return 0
    m, n = len(grid), len(grid[0])
    max_killed = 0
    row_e, col_e = 0, [0] * n
    # iterates over all cells in the grid
    for i in range(m):
        for j in range(n):
            # makes sure we are next to a wall.
            if j == 0 or grid[i][j-1] == 'W':
                row_e = row_kills(grid, i, j)
            # makes sure we are next to a wall.
            if i == 0 or grid[i-1][j] == 'W':
                col_e[j] = col_kills(grid, i, j)
            # makes sure the cell contains a 0
            if grid[i][j] == '0':
                # updates the variable
                max_killed = max(max_killed, row_e + col_e[j])

    return max_killed