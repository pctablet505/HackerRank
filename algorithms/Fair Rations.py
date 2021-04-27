#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fairRations function below.
def fairRations(arr):
    count_odd = 0
    for x in arr:
        if x & 1:
            count_odd += 1
    if count_odd & 1:
        return 'NO'
    d = 0
    f = False
    res = 0
    for i in range(len(arr)):
        if f and arr[i] & 1:
            res += 2 * d + 2
            d = 0
            f = False
        elif f:
            d += 1
        elif arr[i] & 1:
            f = True
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
