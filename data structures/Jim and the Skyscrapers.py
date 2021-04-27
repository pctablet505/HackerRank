#!/bin/python3

import os
import sys


def solve(arr):
    stack = []
    count = 0
    for h in arr:
        while stack and h > stack[-1][0]:
            stack.pop()
        if stack and h == stack[-1][0]:
            count += stack[-1][1]
            stack[-1][1] += 1
        else:
            stack.append([h, 1])
    return 2 * count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
