#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
# Complete the insertionSort1 function below.
def printA(arr):
    for i in arr:
        print(i,end=' ')
    print()
def insertionSort1(n,arr):
    temp=arr[n-1]
    i=n-2
    while arr[i]>temp and i>=0:
        arr[i+1]=arr[i]
        printA(arr)
        i-=1
    arr[i+1]=temp
    printA(arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
