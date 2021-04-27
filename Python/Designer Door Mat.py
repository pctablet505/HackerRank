line = '---'
dot = '.|.'
n, m = map(int, input().split(' '))
i = n // 2;
j = 0
for _ in range(n // 2):
    print(line * i, dot * (2 * j + 1), line * i, sep='')
    i -= 1
    j += 1
i += 1
j -= 1
print('WELCOME'.center(m, '-'))
for _ in range(n // 2):
    print(line * i, dot * (2 * j + 1), line * i, sep='')
    i += 1
    j -= 1
