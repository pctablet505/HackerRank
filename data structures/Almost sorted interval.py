#!/bin/python3

import os
import sys
import bisect


# Complete the solve function below.
def solve(arr):
    n = len(arr)
    ans = 0
    minstack = []
    maxstack = []
    count = 0
    for index, x in enumerate(arr):
        while minstack and arr[minstack[-1]] > x:
            minstack.pop()
        while maxstack and arr[maxstack[-1]] < x:
            maxstack.pop()
        minstack.append(index)
        maxstack.append(index)
        if len(maxstack) == 1:
            count += len(minstack)
        else:
            ind = bisect.bisect(minstack, maxstack[-2])
            count += len(minstack) - ind
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
