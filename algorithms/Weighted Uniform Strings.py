#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    s = s.lower()
    letters = dict()
    for x, y in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)):
        letters[x] = y
    weights = set()
    c = 1
    p = s[0]
    weights.add(letters[p])
    for i in range(1, len(s)):
        if s[i] == p:
            c += 1
            weights.add(letters[p] * c)
        else:

            p = s[i]
            c = 1
            weights.add(letters[p])
    if len(s) > 1 and s[i] != s[i - 1]:
        weights.add(letters[s[i]])
    res = []

    for q in queries:
        if q in weights:
            res.append('Yes')
        else:
            res.append('No')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
