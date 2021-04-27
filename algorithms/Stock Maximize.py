#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(arr):
    n = len(arr)
    max_from_futre = [0] * n
    m = 0
    j = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i] > m:
            m = arr[i]
            j = i
            max_from_futre[i] = j
        max_from_futre[i] = j
    profit = 0
    for i in range(n):

        if arr[i] <= arr[max_from_futre[i]]:
            profit += arr[max_from_futre[i]] - arr[i]
    return profit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
