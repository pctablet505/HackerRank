#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrangeStudents' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def arrangeStudents(a, b):
    a.sort()
    b.sort()
    ia=iter(a)
    ib=iter(b)
    c1=[]
    c2=[]
    d=a+b
    d.sort()
    
    for x in range(len(a)):
        c1.extend([next(ia),next(ib)])
    ia=iter(a)
    ib=iter(b)
    for x in range(len(a)):
        c2.extend([next(ib),next(ia)])
    if c1==d or c2==d:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()
