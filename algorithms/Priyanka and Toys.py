#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the toys function below.
def toys(w):
    w.sort()
    count = 0
    i = 0
    M = sys.maxsize * (-1)
    for i in range(len(w)):
        if w[i] > M:
            M = w[i] + 4
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
