#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def maximumPower(s):
    arr=[x for x in s]
    prev=arr[0]
    j=1
    res=[]
    d=1
    while j<len(arr):
        while j<len(arr) and arr[j]==prev:
            d+=1
            j+=1
        res.append((prev,d))
        if j<len(arr):
            d=1
        else:
            d=0
        if j<len(arr):
            prev=arr[j]
            j+=1
    if d:
        res.append((prev,d))
    length=0
    for l,d in res:
        if l=='0':
            length=max(length,d)
    
    if len(res)>1 and res[0][0]=='0' and res[-1][0]=='0':
        length=max(length,res[0][1]+res[-1][1])
    if '1' in arr:
        return length
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = maximumPower(s)

    fptr.write(str(result) + '\n')

    fptr.close()
