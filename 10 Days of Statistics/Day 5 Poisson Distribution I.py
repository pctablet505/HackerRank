import math

l = float(input())
k = int(input())


def p(k, l):
    return (l ** k) * (math.e) ** (-1 * l) / (math.factorial(k))


print(p(k, l))
