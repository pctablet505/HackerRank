#

def nextMove(n, r, c, grid):
    res = ''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'p':
                princess = (i, j)
                break
    i, j = princess
    if r < i:
        return 'DOWN'
    elif c < j:
        return 'RIGHT'
    elif r > i:
        return 'UP'
    elif c > j:
        return 'LEFT'


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
