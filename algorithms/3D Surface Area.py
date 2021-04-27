#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def area(A,i,j,m,n):
    res=0
    if i-1>=0:
        res+=max(A[i][j]-A[i-1][j],0)
    else:
        res+=A[i][j]
    if i+1<m:
        res+=max(A[i][j]-A[i+1][j],0)
    else:
        res+=A[i][j]
    if j+1<n:
        res+=max(A[i][j]-A[i][j+1],0)
    else:
        res+=A[i][j]
    if j-1>=0:
        res+=max(A[i][j]-A[i][j-1],0)
    else:
        res+=A[i][j]
    return res
    



def surfaceArea(A):
    m=len(A)
    n=len(A[0])
    res=0
    for i in range(m):
        for j in range(n):
            res+=area(A,i,j,m,n)
    res+=2*m*n
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
