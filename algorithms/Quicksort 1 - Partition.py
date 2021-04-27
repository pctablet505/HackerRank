#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p=arr[0]
    left=[]
    right=[]
    equal=[]
    for i in range(len(arr)):
        if arr[i]<p:
            left.append(arr[i])
        elif arr[i]==p:
            equal.append(arr[i])
        else:
            right.append(arr[i])
    result=left+equal+right
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
