n=int(input())
x=list(map(int,input().split()))
f=list(map(int,input().split()))
arr=[]
for i in range(n):
    arr.extend([x[i]]*f[i])
arr.sort()

def findMid(arr):
    mid=len(arr)//2
    if len(arr)&1==0:
        q=(arr[mid-1]+arr[mid])/2
    else:
        q=arr[mid]
    return (q,mid)
q2,m2=findMid(arr)
if len(arr)&1==1:
    q1,m1=findMid(arr[0:m2])
    q3,m3=findMid(arr[m2+1:])
else:
    q1,m1=findMid(arr[0:m2])
    q3,m3=findMid(arr[m2:])
print('{:.1f}'.format(q3-q1))
