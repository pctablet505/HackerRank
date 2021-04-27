from math import ceil, sqrt


def biggestPrimeFactor(n):
    f = 1
    while not n & 1:
        n //= 2
        f = 2
    if n == 1:
        return 2
    i = 3
    while i <= ceil(sqrt(n)):
        if n % i == 0:
            n //= i
            i = 3
        else:
            i += 2
    if n > 2:
        return n
    else:
        return i


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(biggestPrimeFactor(n))
