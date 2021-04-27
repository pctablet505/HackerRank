from math import factorial as f


def comb(n, r):
    return f(n) / (f(n - r) * f(r))


def binomial(x, n, p):
    return comb(n, x) * (p ** x) * (q ** (n - x))


boys, girls = 1.09, 1
p = boys / (boys + girls)
q = 1 - p
ans = 0
for i in range(3, 6 + 1):
    ans += binomial(i, 6, p)
print('{:.3f}'.format(ans))
