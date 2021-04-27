#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr,n):
    max_curr=max_global=arr[0]
    for i in range(1,n):
        max_curr=max(arr[i],max_curr+arr[i])
        max_global=max(max_curr,max_global)
    arr.sort()
    a=b=arr[0]
    for i in range(1,n):
        a=max(arr[i],a+arr[i])
        if b<a:
            b=a
    return (max_global,b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr,n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
