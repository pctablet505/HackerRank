#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy

# Complete the cavityMap function below.
def cavityMap(grid):
    
    res=deepcopy(grid)
    #res=[[x for x in y] for y in grid]
    n=len(grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]:
                res[i]=res[i][:j]+'X'+res[i][j+1:]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
