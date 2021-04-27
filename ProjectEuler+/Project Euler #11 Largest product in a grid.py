grid = [[int(i) for i in input().split()] for x in range(20)]
m = 0
for i in range(20):
    for j in range(20):
        if j < 17:
            n = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            if n > m: m = n
        if i < 17:
            n = grid[j][i] * grid[j][i + 1] * grid[j][i + 2] * grid[j][i + 3]
            if n > m: m = n
        if i < 17 and j < 17:
            n = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if n > m: m = n
        if i > 2 and j < 17:
            n = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
            if n > m: m = n
print(m)
