#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqlist = []
    lastAnswer = 0
    result = []
    for i in range(n):
        seqlist.append([])
    for a, x, y in queries:
        index = (x ^ lastAnswer) % n

        if a == 1:
            seqlist[index].append(y)
        if a == 2:
            size = len(seqlist[index])
            lastAnswer = seqlist[index][y % size]
            result.append(lastAnswer)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
