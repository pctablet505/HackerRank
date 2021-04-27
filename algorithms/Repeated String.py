#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    length=len(s)
    if n<=length:
        res=0
        for i in range(n):
            if s[i]=='a':
                res+=1
        return res
    x=n//length
    count=0
    for i in range(length):
        if s[i]=='a':
            count+=1
    res=0
    res+= x*count
    for i in range(n-x*length):
        if s[i]=='a':
            res+=1
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
