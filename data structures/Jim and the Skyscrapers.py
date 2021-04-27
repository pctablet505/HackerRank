#!/bin/python3

import os
import sys


# Complete the solve function below.
def solve(arr):
    n = len(arr)
    hhs = sorted(enumerate(arr), key=lambda t: (t[1], t[0]))
    prev = list(range(-1, n - 1))
    next = list(range(1, n + 1))
    fi, fh = li, lh = hhs[0]
    boloc_length = 1
    s = 0
    for i, h in hhs[1:]:
        if h == lh and i == next[li]:
            boloc_length += 1
            li = i
        else:
            s += boloc_length * (boloc_length - 1)
            pi, ni = prev[fi], next[li]
            if pi >= 0:
                next[pi] = ni
            if ni < n:
                prev[ni] = pi
            fi, fh = li, lh = i, h
            boloc_length = 1
    s += boloc_length * (boloc_length - 1)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
