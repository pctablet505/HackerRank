#!/bin/python3

import sys
import bisect

l = set()
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        s = str(x)
        if s == s[::-1]:
            l.add(x)
l = sorted(l)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = bisect.bisect_right(l, n)
    # print(x)
    if x < len(l) and l[x] < n:
        print(l[x])
    elif l[x - 1] < n:
        print(l[x - 1])
    else:
        print(l[x - 2])
