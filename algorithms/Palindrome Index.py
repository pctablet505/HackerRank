#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    i=0
    j=len(s)-1
    while i<=j:
        if s[i]==s[j]:
            i+=1
            j-=1
            continue
        
        if s[i+1]==s[j] and s[:i]+s[i+1:]==(s[:i]+s[i+1:])[::-1]:
            return i
        if s[i]==s[j-1] and s[:j]+s[j+1:]==(s[:j]+s[j+1:])[::-1]:
            return j
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
