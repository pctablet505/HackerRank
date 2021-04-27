#!/bin/python3

import math
import os
import random
import re
import sys
import copy


# Complete the minimumLoss function below.
def minimumLoss(price, n):
    p = dict()
    for i in range(n):
        p[price[i]] = i
    arr = copy.deepcopy(price)
    arr.sort()
    mini = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        if p[arr[i - 1]] > p[arr[i]]:
            mini = min(mini, diff)
    return mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price, n)

    fptr.write(str(result) + '\n')

    fptr.close()
