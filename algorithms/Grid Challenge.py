#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    r=len(grid)
    c=len(grid[0])
    g=[]
    for x in grid:
        g.append([y for y in x])
    for x in g:
        x.sort()
    for i in range(c):
        s=[g[x][i] for x in range(r)]
        for j in range(len(s)-1):
            if s[j]<=s[j+1]:
                continue
            return 'NO'
    return 'YES'

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
