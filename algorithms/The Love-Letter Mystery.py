#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    count=0
    a=[x for x in s]
    n=len(a)
    for i in range(n//2):
        c=ord(a[i])-ord(a[n-i-1])
        if c>0:
            a[n-1-i]=chr(ord(a[n-i-1])-c)
        if c<0:
            a[n-1-i]=chr(ord(a[n-1-i])+c)
        count +=abs(c)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
