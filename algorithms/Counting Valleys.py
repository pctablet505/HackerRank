#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    current=0
    previous=0
    for x in s:
        if x=='U':
            current+=1
        elif x=='D':
            current-=1
        if previous>=0 and current<0:
            count+=1
        previous=current
    return count
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
