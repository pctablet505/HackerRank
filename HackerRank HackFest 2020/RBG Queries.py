#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mixColors' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY colors
#  2. 2D_INTEGER_ARRAY queries
#

def mixColors(colors, queries):
    from collections import defaultdict
    red=defaultdict(set)
    blue=defaultdict(set)
    green=defaultdict(set)
    for r,b,g in colors:
        red[r].add((r,b,g))
        blue[b].add((r,b,g))
        green[g].add((r,b,g))
    result=[]
    for r,b,g in queries:
        reds=False
        blues=False
        greens=False
        for x,y,z in red[r]:
            if y<=b and z<=g:
                reds=True
                break
        for x,y,z in blue[b]:
            if x<=r and z<=g:
                blues=True
                break
        for x,y,z in green[g]:
            if x<=r and y<=b:
                greens=True
                break
        if reds and blues and greens:
            result.append('YES')
        else:
            result.append('NO')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    colors = []

    for _ in range(n):
        colors.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = mixColors(colors, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
