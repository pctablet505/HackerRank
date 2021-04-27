#!/bin/python3

import math
import os
import random
import re
import sys


def diff(arr1, arr2):
    res = 0
    print(len(arr1), len(arr2))
    for i in range(9):
        res += abs(arr1[i] - arr2[i])
    return res


arr = []
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for x1 in s:
    for x2 in s - {x1}:
        x3 = 15 - (x1 + x2)
        if x3 in s - {x1, x2}:
            for x4 in s - {x1, x2, x3}:
                x7 = 15 - (x1 + x4)
                if x7 in s - {x1, x2, x3, x4}:
                    for x5 in s - {x1, x2, x3, x4, x7}:
                        x6 = 15 - (x4 + x5)
                        if x6 in s - {x1, x2, x3, x4, x5, x7}:
                            x8 = 15 - (x2 + x5)
                            if x8 in s - {x1, x2, x3, x4, x5, x6, x7}:
                                x9 = 15 - (x1 + x5)
                                if x9 in s - {x1, x2, x3, x4, x5, x7, x8}:
                                    if (x1 + x2 + x3) == (x4 + x5 + x6) == (x7 + x8 + x9) == (x1 + x4 + x7) == (
                                            x2 + x5 + x8) == (x3 + x6 + x9) == (x1 + x5 + x9) == (x7 + x5 + x3) == 15:
                                        arr.append([x1, x2, x3, x4, x5, x6, x7, x8, x9])


def formingMagicSquare(s):
    global arr
    arrc = []
    for x in s:
        arrc += x
    return min([diff(x, arrc) for x in arr])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
