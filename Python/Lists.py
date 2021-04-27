alist = []
commands = []
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        commands.append(input().split())

for command in commands:
    if command[0] == 'print':
        print(alist)
    if command[0] == 'insert':
        alist.insert(int(command[1]), int(command[2]))
    if command[0] == 'remove':
        alist.remove(int(command[1]))
    if command[0] == 'append':
        alist.append(int(command[1]))
    if command[0] == 'sort':
        alist.sort()
    if command[0] == 'pop':
        alist.pop()
    if command[0] == 'reverse':
        alist.reverse()
'''print(commands)'''
