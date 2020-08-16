from itertools import product
K, M=map(int,input().split())
arr=[]
for _ in range(K):
    arr.append(list(map(int,input().split()))[1:])

sets=(list(product(*arr)))
values=[]
for x in sets:
    sumsquare=0
    for y in x:
        sumsquare+=y**2
    values.append(sumsquare%M)
print(max(values))
