#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the shortPalindrome function below.
def shortPalindrome(s):
    n = len(s)
    count = 0
    mod = 10 ** 9 + 7
    singles = [0] * 26
    doubles = [0] * 26 * 26
    triples = [0] * 26 * 26
    base = ord('a')
    r26 = [i for i in range(26)]
    for c in s:
        ind = ord(c) - base
        p = 26 * ind - 1
        q = ind - 26
        for i in r26:
            q += 26
            p += 1
            count += triples[q]
            triples[p] += doubles[p]
            doubles[p] += singles[i]
        singles[ind] += 1
    return count % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
