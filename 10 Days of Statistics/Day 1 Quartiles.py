n=int(input())
arr=list(map(int,input().split()))
arr.sort()
def findMid(arr):
    mid=len(arr)//2
    if len(arr)&1==0:
        q=(arr[mid-1]+arr[mid])/2
    else:
        q=arr[mid]
    return (q,mid)
q1,m1=findMid(arr)
if len(arr)&1==1:
    q0,m0=findMid(arr[0:m1])
    q2,m2=findMid(arr[m1+1:])
else:
    q0,m0=findMid(arr[0:m1])
    q2,m2=findMid(arr[m1:])
print(int(q0),int(q1),int(q2),sep='\n')
