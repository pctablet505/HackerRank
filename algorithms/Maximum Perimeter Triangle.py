#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks.sort()
    n = len(sticks)
    a, b, c = 0, 0, 0
    p = 0
    for i in range(n - 2):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            p1 = sticks[i] + sticks[i + 1] + sticks[i + 2]
            if p1 > p:
                p = sticks[i] + sticks[i + 1] + sticks[i + 2]
                a, b, c = sticks[i], sticks[i + 1], sticks[i + 2]
    return (a, b, c) if a and b and c else [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
