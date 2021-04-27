#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    res=0
    i=0
    while i<len(c):
        if i<len(c)-2:
            if c[i+2]==0:
                i+=2
                res+=1
            elif c[i+1]==0:
                i+=1
                res+=1
        else:
            i+=1
            res+=1

        if i==len(c)-1:
            break
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
