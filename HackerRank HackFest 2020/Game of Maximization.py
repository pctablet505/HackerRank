#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maximumStones(arr):
    i=0
    odd=[]
    even=[]
    for i in range(1,len(arr),2):
        odd.append(arr[i])
    for i in range(0,len(arr),2):
        even.append(arr[i])
    return min(sum(odd),sum(even))*2
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
