#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the findConnectedComponents function below.
def countSetBits(n):
    c = 0
    while n:
        if n & 1:
            c += 1
        n >>= 1
    return c


def findConnectedComponents(d):
    d = list(set(d))
    n = len(d)
    count = 0
    for i in range(n + 1):
        for s in combinations(d, i):
            dj = []
            av = set(s)
            while av:
                mask = av.pop()
                temp = []
                for x in av:
                    if mask & x:
                        mask |= x
                        temp.append(x)
                dj.append(mask)
                while temp:
                    av.discard(temp.pop())
            count += 64 + len(dj) - sum([countSetBits(x) for x in dj])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()
