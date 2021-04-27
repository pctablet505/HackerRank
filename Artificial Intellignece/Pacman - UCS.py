from collections import defaultdict, deque

pacman = tuple(map(int, input().split()))
food = tuple(map(int, input().split()))
m, n = map(int, input().split())

matrix = []

for i in range(m):
    matrix.append([x for x in input()])

visited = set()
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

arr = []
flag = False
parent = defaultdict(lambda: None)
parent[pacman] = None

queue = deque()
queue.append(pacman)

while queue:
    if flag:
        break
    u = queue.popleft()
    arr.append(u)

    i, j = u
    if u == food:
        flag = True
        break
    for x, y in moves:
        v = i + x, j + y
        if 0 <= v[0] < m and 0 <= v[1] < n:
            x, y = v
            if v not in visited and matrix[x][y] in '-.':
                parent[v] = u
                queue.append(v)
                visited.add(v)

path = []
x = food
while x != None:
    path.append(x)
    x = parent[x]
path.reverse()

print(len(path) - 1)
for x, y in path:
    print(x, y)
