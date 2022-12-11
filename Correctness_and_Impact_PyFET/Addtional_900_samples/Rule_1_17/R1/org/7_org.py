def dfs(maze, i, j, depth, cnt):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    row = len(maze)
    col = len(maze[0])

    if i == row - 1 and j == col - 1 and col > 10 and row > 10:
        if cnt == -1:
            cnt = depth
        else:
            if cnt > depth:
                cnt = depth
        return cnt

    maze[i][j] = 0

    for k in range(len(directions)):
        nx_i = i + directions[k][0]
        nx_j = j + directions[k][1]

        if nx_i >= 0 and nx_i < row and nx_j >= 0 and nx_j < col:
            if maze[nx_i][nx_j] == 1:
                cnt = dfs(maze, nx_i, nx_j, depth + 1, cnt)

    maze[i][j] = 1

    return cnt
