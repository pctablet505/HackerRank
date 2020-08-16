n1=int(input())
a=set(map(int,input().split()))
n2=int(input())
b=set(map(int,input().split()))
c=set()
c.update((a.union(b)).difference((a.intersection(b))))
for x in sorted(c):
    print(x)
