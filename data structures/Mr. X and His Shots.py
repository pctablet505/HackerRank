class BIT:
    def __init__(self,size):
        self.BITree=[0]*(size+1)
    def add(self,i,val):
        while i<=self.BITree.__len__():
            self.BITree[i-1]+=val;
            i+=i&(-i)
    def getSum(self,i):
        s=0
        while i>0:
            s+=self.BITree[i-1]
            i-=i&(-i)
        return s

N,M=map(int,input().split())
a=BIT(10**5)
b=BIT(10**5)
for i in range(N):
    x,y=map(int,input().split())
    a.add(x,1)
    b.add(y,1)
s=0
for i in range(M):
    x,y=map(int,input().split())
    s+=(M-b.getSum(x-1)-(M-a.getSum(y)))
print(s)
