from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
array = (list(map(int, stdin.readline().split())))
string = ''.join(chr(96 + n) for n in array)
for i in range(M):
    q, i, j = map(int, stdin.readline().split())
    if q == 1:
        if i > 1:
            string = string[i - 1:j] + string[:i - 1] + string[j:]
    if q == 2:
        string = string[0:i - 1] + string[j:] + string[i - 1:j]
start = ord(string[0]) - 97;
end = ord(string[-1]) - 97
print(abs(start - end))
for i in range(N):
    print(ord(string[i]) - 96, end=' ')
