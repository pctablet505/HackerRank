#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for x in arr:
        if x>0:pos+=1
        elif x==0:zer+=1
        else:neg+=1
    print('{:.6f}'.format(pos/(pos+neg+zer)))
    print('{:.6f}'.format(neg/(pos+neg+zer)))
    print('{:.6f}'.format(zer/(pos+neg+zer)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
