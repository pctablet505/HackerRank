#!/bin/python3

import sys
from math import sqrt, ceil


def fun(n):
    M = -1
    for a in range(1, n // 3 + 1):
        b = (((n ** 2) // 2) - a * n) // (n - a)
        c = n - (a + b)
        if (a + b + c) == n and a * a + b * b == c * c:
            M = max(M, a * b * c)
    return M


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fun(n))
