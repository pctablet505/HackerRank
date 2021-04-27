#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestIncreasingSubsequence function below.
def CeilIndex(arr,l,r,key):
    while r-l>1:
        m=l+(r-l)//2
        if arr[m]>=key:
            r=m
        else:
            l=m
    return r
def longestIncreasingSubsequence(arr):
    n=len(arr)
    tailTable=[0]*(n)
    length=0
    tailTable[0]=arr[0]
    length=1
    
    for i in range(1,n):
        if arr[i]<=tailTable[0]:
            tailTable[0]=arr[i]
        elif arr[i]>tailTable[length-1]:
            tailTable[length]=arr[i]
            length+=1
        else:
            tailTable[CeilIndex(tailTable,0,length-1,arr[i])]=arr[i]
        
    return length        







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
