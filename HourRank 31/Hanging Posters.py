#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

def solve(h, wallPoints, lengths):
    min=0
    for i in range(len(wallPoints)):
        temp=wallPoints[i]-h-lengths[i]/4
        if temp>min:
            min=temp
    
    if min%1>0:
        min=min//1+1
    return int(min)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    fptr.write(str(answer) + '\n')

    fptr.close()
