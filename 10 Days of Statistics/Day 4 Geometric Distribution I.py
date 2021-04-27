def g(n,p):
    return p*(1-p)**(n-1)
nu,du=map(int,input().split())
p=nu/du
n=int(input())
print('{:.3f}'.format(g(n,p)))
