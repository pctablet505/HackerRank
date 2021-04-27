#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the equal function below.
def equal(arr):
    i = 0
    m = min(arr)
    arr.sort()
    ans = float('inf')
    count = 0
    for b in range(3):
        cs = 0
        for i in range(len(arr)):
            d = arr[i] - arr[0] + b
            cs += int(d / 5) + (d % 5) // 2 + d % 5 % 2
        ans = min(ans, cs)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
