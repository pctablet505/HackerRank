#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    num = [int(x) for x in num]
    i = 0
    p = 0
    M = 0
    for i in range(n - k):
        if p != 0:
            M = max(M, p)
            p //= num[i - 1]
            p *= num[i + k - 1]
        else:
            p = 1
            for x in num[i:i + k]:
                p *= x
            M = max(M, p)
    print(M)
