#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy


def minimumSwaps(arr):
    arrs = sorted(arr)
    c = 0
    ref = dict()
    for i in range(len(arr)):
        ref[arr[i]] = i
    for i in range(len(arr)):
        if arr[i] != arrs[i]:
            p = ref[arrs[i]]
            c += 1
            arr[i], arr[p] = arr[p], arr[i]
            ref[arr[i]] = i
            ref[arr[p]] = p
    return c


def lilysHomework(arr):
    return min(minimumSwaps(deepcopy(arr)), minimumSwaps(deepcopy(arr)[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
