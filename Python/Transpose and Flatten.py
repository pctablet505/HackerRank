import numpy as np
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a=np.array(a)
print(np.transpose(a))
print(a.flatten())



