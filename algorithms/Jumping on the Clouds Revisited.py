#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    l = len(c)
    e = 100
    while e >= 0:
        print(i, e, c[(i + k) % l])
        if c[(i + k) % l] == 1:
            e -= 3
        else:
            e -= 1
        i += k
        if i % l == 0:
            break
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
