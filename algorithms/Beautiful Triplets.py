#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(x, arr):
    d = [False] * ((2 * 10 ** 4) + 50)
    for y in arr:
        d[y] = True
    c = 0
    for n in arr:
        if d[n + x] and d[n + 2 * x]:
            c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
