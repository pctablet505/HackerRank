#!/bin/python3

from math import ceil,floor
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def clique(n, m):
    M=0
    l=0
    h=n
    while l<=h:
        i=ceil((l+h)/2)
        if m>(0.5*(n**2 -(n%i)*ceil(n/i)**2-(i-(n%i))*floor(n/i)**2)):
            M=i+1
            l=i+1
        else:
            h=i-1
    return M




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
