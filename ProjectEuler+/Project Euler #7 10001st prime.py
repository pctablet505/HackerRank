#!/bin/python3

import sys

arr = [True for i in range(1000000)]
for i in range(2, len(arr)):
    for j in range(i + i, len(arr), i):
        arr[j] = False
primes = []
for i in range(2, len(arr)):
    if arr[i]:
        primes.append(i)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n - 1])
