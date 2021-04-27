#!/bin/python3

import math
import os
import random
import re
import sys
import heapq


# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    imp = []
    for x in contests:
        if x[1] == 0:
            luck += x[0]
        else:
            imp.append(x[0])
    luck -= sum(imp)
    luck += 2 * sum(heapq.nlargest(k, imp))
    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
