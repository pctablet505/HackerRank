#!/bin/python3

import math
import os
import random
import re
import sys


def reduce(string):
    flag = False
    s = ''
    i = 0
    n = len(string)
    while i < n:
        if i + 1 < n:
            if string[i] == string[i + 1]:
                i += 2
                flag = True
                continue
        s += string[i]
        i += 1
    if s and flag:
        return reduce(s)
    else:
        return s


def superReducedString(string):
    s = reduce(string)
    if s:
        return s

    return 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
