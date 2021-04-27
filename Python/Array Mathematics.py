from numpy import array as arr

N, M = map(int, input().split())
for _ in range(N):
    a = arr(list(list(map(int, input().split())) for _ in range(N)))
    b = arr(list(list(map(int, input().split())) for _ in range(N)))
    print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')
