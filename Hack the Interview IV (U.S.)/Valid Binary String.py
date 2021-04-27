#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER 
#

def minimumMoves(s, d):
    s=[x for x in s]
    c=0
    l=len(s)
    i=0
    while i<l-d+1:
        for j in range(i+d-1,i-1,-1):
            if s[j]=='1':
                i=j
                break
        
        if j==i and s[j]!='1':
            s[i+d-1]='1'
            c+=1
        i+=1
    return c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()
