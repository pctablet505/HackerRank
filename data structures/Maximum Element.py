stack1 = []
stack2 = []
n = int(input())
for _ in range(n):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        if len(stack2) == 0:
            stack1.append(query[1])
            stack2.append(query[1])
        else:
            stack1.append(query[1])
            if stack2[-1] >= query[1]:
                stack2.append(stack2[-1])
            else:
                stack2.append(query[1])
    if query[0] == 2:
        stack1.pop()
        stack2.pop()
    if query[0] == 3:
        print(stack2[-1])
