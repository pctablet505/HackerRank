N = int(input())
p = list(map(int, input().split(' ')))
days = [0] * N
s = [0]
mi = p[0]
ma = 0
for i in range(1, N):
    if p[i] > p[i - 1]:
        days[i] = 1
    mi = min(mi, p[i])
    while s and p[s[-1]] >= p[i]:
        if p[i] > mi:
            days[i] = max(days[i], days[s[-1]] + 1)
        s.pop()
    ma = max(ma, days[i])
    s += [i]
print(ma)
