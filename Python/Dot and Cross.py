import numpy as np

n = int(input())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))
a = np.array(a)
b = np.array(b)
print(np.dot(a, b))
