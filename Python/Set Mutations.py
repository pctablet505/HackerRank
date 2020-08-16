nA=int(input())
A=set(map(int,input().split()))
no=int(input())
for _ in range(no):
    eval('A.{}({})'.format(input().split()[0],set(map(int,input().split()))))
print(sum(A))
