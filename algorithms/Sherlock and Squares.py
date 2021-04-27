#!/bin/python3

from math import sqrt, ceil,floor
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    x=ceil(sqrt(a))
    y=floor(sqrt(b))
    count=0
    count+=y-x
    if x>y:
        return 0
    if y**2<=b:
        count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
