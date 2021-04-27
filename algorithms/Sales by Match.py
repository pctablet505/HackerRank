#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    count = 0
    c = Counter(arr)
    for x in c:
        count += (c[x] // 2)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
