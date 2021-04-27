#!/bin/python3

import os
import sys

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    n=a**b
    l=x*(n//x)
    u=x*((n//x)+1)
    if abs(l-n)>abs(u-n):
        return u
    else:
        return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = int(closestNumber(a, b, x))

        fptr.write(str(result) + '\n')

    fptr.close()
