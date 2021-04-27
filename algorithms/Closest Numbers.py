#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    res=[]
    minimum=float('inf')
    for i in range(len(arr)-1):
        diff=arr[i+1]-arr[i]
        if diff<minimum:
            minimum=diff
            res=[arr[i],arr[i+1]]
        elif diff==minimum:
            res.extend([arr[i],arr[i+1]])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
