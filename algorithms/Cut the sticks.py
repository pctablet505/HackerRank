#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

def cutTheSticks(arr):
    heapq.heapify(arr)
    res=[len(arr)]
    while arr:
        smallest=heapq.heappop(arr)
        while arr and arr[0]==smallest:
            heapq.heappop(arr)
        res.append(len(arr))
        for i in range(len(arr)):
            arr[i]-=smallest
    res.pop()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
