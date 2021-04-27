#

def solve(grid):
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'p':
                princess = (i, j)
            if grid[i][j] == 'm':
                bot = (i, j)

    i, j = princess
    r, c = bot

    while r < i:
        res.append('DOWN')
        r += 1
    while c < j:
        res.append('RIGHT')
        c += 1
    while r > i:
        res.append('UP')
        r -= 1
    while c > j:
        res.append('LEFT')
        c -= 1
    return res


n = int(input())

grid = []
for i in range(0, n):
    grid.append([x for x in input()])

for x in solve(grid):
    print(x)
