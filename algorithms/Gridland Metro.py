#!/bin/python3

import math
import os
import random
import re
import sys
def mergeRange(arr):
    arr.sort(key=lambda x:x[0])
    stack=[]
    stack.append(arr[0])
    for x in arr:
        if x[0]<=stack[-1][1]:
            stack[-1][1]=max(stack[-1][1],x[1])
        else:
            stack.append(x)
    return stack


# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    track.sort(key=lambda x:x[0])
    av=m*n
    i=0
    while i<len(track):
        row=track[i][0]
        s=[]
        while i<len(track) and track[i][0]==row:
            s.append([track[i][1],track[i][2]])
            i+=1
        s=mergeRange(s)
        for l,r in s:
            av-=r-l+1
    return av




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
