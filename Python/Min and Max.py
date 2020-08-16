import numpy as np

n,m=map(int,input().split())
a1=[]
for _ in range(n):
    a1.append(list(map(int,input().split())))
ar1=np.array(a1)
print(max(np.min(a1,axis=1)))
