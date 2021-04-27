# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
for i in range(int(input())):
    command = input().split()
    if len(command) == 2:
        eval('d.{}({})'.format(command[0], command[1]))
    else:
        eval('d.{}()'.format(command[0]))
for item in d:
    print(item, end=' ')
