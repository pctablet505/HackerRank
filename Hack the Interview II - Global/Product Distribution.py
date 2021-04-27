#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    a.sort()
    s = 1
    n = len(a)
    c = 0
    i = 0
    while i < n:
        if n - i >= m:
            c += s * sum(a[i:i + m])
            s += 1
            i += m
        else:
            break
    c += (s - 1) * sum(a[i:])
    return c % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)

    fptr.write(str(ans) + '\n')

    fptr.close()
