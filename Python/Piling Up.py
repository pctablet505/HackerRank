from collections import deque
for _ in range(int(input())):
    n=int(input())
    d=deque(list(map(int,input().split())))
    stack=[]
    for i in range(n):
        if d[0]>=d[-1]:
            a=d.popleft()
        elif d[0]<d[-1]:
            a=d.pop()
        if len(stack)==0:
            stack.append(a)
        elif stack[-1]>=a:
            stack.append(a)            
    if len(stack)==n:
        print("Yes")
    else:
        print("No")
