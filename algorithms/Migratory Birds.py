#!/bin/python3
from operator import itemgetter
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d={}
    for i in range(1,6):
        d[i]=0
    for x in arr:
        d[x]=d.get(x)+1
    return(max(d.items(),key=itemgetter(1))[0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
