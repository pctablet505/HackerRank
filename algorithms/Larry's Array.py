#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the larrysArray function below.
def larrysArray(A, n):
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                c += 1

    return 'YES' if not (c & 1) else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A, n)

        fptr.write(result + '\n')

    fptr.close()
