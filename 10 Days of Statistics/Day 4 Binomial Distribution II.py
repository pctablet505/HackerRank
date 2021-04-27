p, n = map(int, input().split())
p /= 100
q = 1 - p
# p is the probablity of defect
from math import factorial as f


def comb(n, r):
    return f(n) / (f(n - r) * f(r))


def binomial(x, n, p):
    return comb(n, x) * (p ** x) * (q ** (n - x))


ans1 = 0
ans2 = 0
for i in range(3):
    ans1 += binomial(i, n, p)
print('{:.3f}'.format(ans1))
for i in range(2, n + 1):
    ans2 += binomial(i, n, p)
print('{:.3f}'.format(ans2))
