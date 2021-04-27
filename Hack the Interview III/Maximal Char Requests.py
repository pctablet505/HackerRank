#!/bin/python3

import math
import os
import random
import re
import sys

from copy import deepcopy

C = [0] * 26


def index(ch):
    return ord(ch) - ord('a')


def maximum(C):
    for i in range(25, -1, -1):
        if C[i] > 0:
            return i


def getMaxCharCount(s, queries):
    s = s.lower()
    n = len(s)
    res = []
    countArray = [C for _ in range(n)]
    countArray[0][index(s[0])] = 1
    for i in range(1, n):
        countArray[i] = deepcopy(countArray[i - 1])
        ind = index(s[i])
        countArray[i][ind] += 1
    for l, r in queries:
        if l == 0:
            letter = maximum(countArray[r])
            res.append(countArray[r][letter])
        else:
            result = []
            for i in range(26):
                result.append(countArray[r][i] - countArray[l - 1][i])
            letter = maximum(result)
            res.append(result[letter])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    q = int(input().strip())

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    ans = getMaxCharCount(s, query)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
