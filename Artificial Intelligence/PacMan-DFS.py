from collections import defaultdict

'''pacman=tuple(map(int,input().split()))
food=tuple(map(int,input().split()))
m,n=map(int,input().split())
'''

pacman = 3, 9
food = 5, 1
m, n = 7, 20
matrix = [['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%'],
          ['%', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '%', '-', '-', '-', '%'],
          ['%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '%', '-', '%', '-', '%'],
          ['%', '-', '-', '-', '-', '-', '-', '-', '-', 'P', '-', '-', '-', '-', '-', '-', '-', '%', '-', '%'],
          ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '-', '%'],
          ['%', '.', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '%'],
          ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%']]
'''
for i in range(m):
    matrix.append([x for x in input()])
'''

explored = []
visited = set()
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

arr = []
flag = False
parent = defaultdict(lambda: None)
parent[pacman] = None

stack = [pacman]

while stack:
    if flag:
        break
    u = stack.pop()
    arr.append(u)
    explored.append(u)
    visited.add(u)
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
                stack.append(v)

path = []
x = food
while x != None:
    path.append(x)
    x = parent[x]
path.reverse()
print(len(explored))
for x, y in explored:
    print(x, y)
print(len(path) - 1)
for x, y in path:
    print(x, y)
