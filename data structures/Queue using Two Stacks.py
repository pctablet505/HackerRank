stack1 = []
stack2 = []


def queuePop():
    if len(stack2) > 0:
        return stack2.pop()
    if len(stack2) == 0:
        while len(stack1) > 0:
            stack2.append(stack1.pop())
        return stack2.pop()


def peek():
    y = queuePop()
    stack2.append(y)
    return y


for _ in range(int(input())):
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack1.append(command[1])
    elif command[0] == 2:
        queuePop()
    elif command[0] == 3:
        print(peek())
