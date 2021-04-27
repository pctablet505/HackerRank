#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.
def icecreamParlor(m, a):
    for i, cost in enumerate(a):
        if (m - cost) in a[i + 1:]:
            return (i + 1, a[i + 1:].index(m - cost) + i + 1 + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
