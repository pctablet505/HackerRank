#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gemstones function below.
def gemstones(arr):
    c = 0
    for x in 'abcdefghijklmnopqrstuvwxyz':
        y = list(map(lambda y: x in y, arr))
        if all(y):
            c += 1

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
