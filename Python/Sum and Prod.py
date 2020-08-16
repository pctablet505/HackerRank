import numpy as np
n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
a=np.array(a)
print(np.prod(np.sum(a,axis=0)))
