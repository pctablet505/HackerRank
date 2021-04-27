#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini=maxi=scores[0]
    m=M=0
    for i in range(1,len(scores)):
        if scores[i]<mini:
            mini=scores[i]
            m+=1
        if scores[i]>maxi:
            maxi=scores[i]
            M+=1
    return (M,m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
