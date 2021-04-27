import numpy as np

n, m, p = map(int, input().split())
a1 = []
a2 = []
for _ in range(n):
    a1.append(list(map(int, input().split())))
for _ in range(m):
    a2.append(list(map(int, input().split())))
ar1 = np.array(a1)
ar2 = np.array(a2)
print(np.reshape(np.concatenate((ar1, ar2)), ((m + n), 2)))
