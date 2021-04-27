def g(n,p):
    return p*(1-p)**(n-1)
nu,du=map(int,input().split())
p=nu/du
n=int(input())
ans=0
for i in range(1,n+1):
    ans+=g(i,p)
print('{:.3f}'.format(ans))
