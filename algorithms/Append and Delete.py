#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    ls=len(s)
    lt=len(t)
    if k>=len(s)+len(t):
        return 'Yes'
    i=0
    m=min(ls,lt)
    while i<m and s[i]==t[i]:
        i+=1
    d=ls+lt-2*i
    if k<d:
        return 'No'
    if k==d:
        return 'Yes'
    if (k-d)%2:
        return 'No'
    else:
        return 'Yes'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
