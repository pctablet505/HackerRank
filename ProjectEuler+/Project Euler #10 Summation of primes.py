#!/bin/python3

import sys
from bisect import bisect_left

arr = [True for i in range(10 ** 6 + 1)]
for i in range(2, len(arr)):
    for j in range(i + i, len(arr), i):
        arr[j] = False
primes = []
for i in range(2, len(arr)):
    if arr[i]:
        primes.append(i)
sums = [primes[0]]
for x in primes[1:]:
    sums.append(sums[-1] + x)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = bisect_left(primes, n + 1)
    print(sums[p - 1])
