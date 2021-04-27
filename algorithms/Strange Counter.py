#!/bin/python3

from math import log2, ceil
import os
import random
import re
import sys


# Complete the strangeCounter function below.
def strangeCounter(n):
    i = ceil(log2((n / 3) + 1))

    s = 3 * (2 ** (i - 1) - 1) + 1
    c0 = 3 * 2 ** (i - 1)

    return s - (n - c0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
