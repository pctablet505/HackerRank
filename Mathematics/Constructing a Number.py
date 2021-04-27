#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the canConstruct function below.
def canConstruct(a):
    s = 0
    for x in a:
        s += sum([int(y) for y in str(x)])
    if s % 3 == 0:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
