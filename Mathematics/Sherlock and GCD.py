#!/bin/python3

import os
import sys
from math import gcd


# Complete the solve function below.
def solve(a):
    n = len(a)
    for i in range(n):
        s = set()
        x = a[i]
        for j in range(i + 1, n):
            x = gcd(x, a[j])
            if x == 1:
                return "YES"
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
