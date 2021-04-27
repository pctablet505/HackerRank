#!/bin/python3

import sys


def Getlcm(n1, n2):
    if n1 > n2:
        n = n1
        d = n2
    else:
        n = n2
        d = n1
    r = n % d
    while r != 0:
        n = d
        d = r
        r = n % d
    gcd = d
    lcm = int(int(n1 * n2) / int(gcd))
    return lcm


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    for j in range(2, n + 1):
        i = Getlcm(i, j)
    print(i)
