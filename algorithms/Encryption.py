#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    s.replace(' ', '')
    L = len(s)
    row = math.floor(math.sqrt(L))
    column = math.ceil(math.sqrt(L))
    if row * column < L:
        row += 1
    arr = [[] for i in range(column)]
    iterator = iter(s)
    print(row, column)
    for x in range(row):
        for y in range(column):
            try:
                arr[y].append(next(iterator))
            except:
                break

    res = ''
    for x in arr:
        res += ''.join(x) + ' '
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
