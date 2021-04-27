#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    d = [0] * n
    d[0] = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            d[i] = d[i - 1] + 1
        else:
            d[i] = 1
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            d[i - 1] = max(d[i] + 1, d[i - 1])

    return sum(d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
