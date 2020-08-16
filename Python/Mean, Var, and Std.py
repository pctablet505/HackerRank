import numpy as np
n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr=np.array(arr)
np.set_printoptions(sign=' ',legacy='1.13')
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr))


