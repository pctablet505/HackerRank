#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.

def workbook(n, k, arr):
    special=0
    p=1
    for no_prob in arr:
        no_pages=math.ceil(no_prob/k)
        q=1
        pi=p
        for x in range(pi,pi+no_pages):
            print(x,q,min(no_prob,q+k))
            if x in range(q,min(no_prob+1,q+k)):
                special+=1
            if q+k<=no_prob:
                q+=k
            else:
                q=no_prob+1
        p+=no_pages
    return special



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
