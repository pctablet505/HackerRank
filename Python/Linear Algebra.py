import numpy as np

mat = []
for _ in range(int(input())):
    mat.append(list(map(float, input().split())))
det = np.linalg.det(mat)
print(round(det, 2))
