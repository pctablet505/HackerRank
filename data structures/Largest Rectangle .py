#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    h.append(0)
    max_area = len(h)
    for i in range(len(h)):
        left_index = i
        while stack and stack[-1][0] >= h[i]:
            last = stack.pop()
            left_index = last[1]
            max_area = max(max_area, h[i] * (i + 1 - left_index), last[0] * (i - left_index))
        stack.append((h[i], left_index))
    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
