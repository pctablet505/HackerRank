n = int(input())
s = set(map(int, input().split()))
no_of_commands=int(input())
for _ in range(no_of_commands):
    eval('s.{}({})'.format(*input().split()+[' ']))
print(sum(s))
