#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    if len(s) == 1:
        return s
    return solve(str(sum([int(x) for x in s])))


def superDigit(n, k):
    return solve(str(sum([int(x) for x in n]) * k))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
