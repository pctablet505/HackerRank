#!/bin/python3

import os
import sys


#
# Complete the solve function below.
#
def solve(t):
    n = len(t)
    a = [0] * (10 ** 6 + 7)
    for i in range(n):
        if t[i] != 0 and t[i] != n:
            a[i + 1] += 1
            a[(i - t[i] + n + 1) % n] -= 1
    max_sum = (float('-inf'))
    s = 0
    max_ind = 1
    for i in range(n):
        s += a[i]
        if s > max_sum:
            max_sum = s
            max_ind = i + 1
    return max_ind


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
