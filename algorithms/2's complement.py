#!/bin/python3

import os
import sys


#
# Complete the twosCompliment function below.
#
def twosCompliment(a, b):
    h1 = a
    h2 = b + 1
    count = 0
    for i in range(32):
        p = 2 ** i
        sum_b = (h2 // (2 * p)) * p + max(0, (h2 % (2 * p)) - p)
        sum_a = (h1 // (2 * p)) * p + max(0, (h1 % (2 * p)) - p)
        count += (sum_b - sum_a)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = twosCompliment(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
