#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    c = Counter(arr)
    M = c.most_common(1)

    return len(arr) - M[0][1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
