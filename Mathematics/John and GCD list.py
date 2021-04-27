#!/bin/python3

import os
import sys
from math import gcd

def lcm(a,b):
    '''lcm(a,b)=[a*b]/[gcd(a,b)]'''
    return a//(gcd(a,b))*b
def solve(a):
    res=[0]*(len(a)+1)
    res[0]=a[0]
    res[-1]=a[-1]
    for i in range(len(a)-1):
        res[i+1]=lcm(a[i],a[i+1])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
