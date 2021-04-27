#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    M=0
    heapq.heapify(c)
    if len(c)>=2:
        m1,m2=heapq.nsmallest(2,c)
    else:
        return max([abs(c[0]-i) for i in range(n)])
    
    i=0
    while i<n:
        if i<=m1 and i<=m2:
            M=max(M,m1-i)
        elif i>m1 and i<=m2:
            M=max(M,min(i-m1,m2-i))
        elif i>m2 and len(c)>2:
            heapq.heappop(c)
            m1,m2=heapq.nsmallest(2,c)
            continue
        else:
            M=max(M,i-m2)

        i+=1
    return M


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
