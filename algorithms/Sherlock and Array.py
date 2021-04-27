#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the balancedSums function below.
def balancedSums(arr):
    n = len(arr)
    sums = [0] * n
    sums[0] = arr[0]
    for i in range(n):
        sums[i] = sums[i - 1] + arr[i]
    print(sums)
    if n == 1:
        return "YES"
    for i in range(n - 1):
        if i == 0:
            if sums[n - 1] - sums[i] == 0:
                return "YES"
        if sums[i - 1] == sums[n - 1] - sums[i]:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
