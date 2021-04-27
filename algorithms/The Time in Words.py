#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the timeInWords function below.
def timeInWords(h, m):
    n = [x for x in range(1, 21)]
    y = 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fiveteen sixteen seventeen eighteen nineteen twenty'.split()
    # print(n,y)
    d = dict(zip(n, y))
    d[30] = 'thirty'
    for i in range(1, 10):
        d[20 + i] = d[20] + ' ' + d[i]
    # print(d)
    if m == 0:
        return d[h] + ' o\' clock'

    if m == 15:
        return 'quarter past ' + d[h]
    if m == 30:
        return 'half past ' + d[h]
    if m == 1:
        return 'one minute past ' + d[h]
    if m < 30:
        return d[m] + ' minutes past ' + d[h]
    else:
        if m == 45:
            return 'quarter to ' + d[h + 1]
        if m < 59:
            return d[60 - m] + ' minutes to ' + d[h + 1]
        if m == 59:
            return 'one minute to ' + d[h + 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
