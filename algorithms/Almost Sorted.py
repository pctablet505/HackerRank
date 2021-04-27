#!/bin/python3

import math
import os
import random
import re
import sys

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            continue
        return False
    else:
        return True



def almostSorted(arr):
    if isSorted(arr):
        print('yes')
        return
    i=0
    original=[x for x in arr]
    for k in range(len(arr)-1):
        if arr[k]>arr[k+1]:
            i=k
            break
    j=i+1
    while arr[j]<arr[i] and j<len(arr)-1:
        j+=1
    if j!=len(arr)-1:
        arr[j-1],arr[i]=arr[i],arr[j-1]
        if isSorted(arr):
            print('yes')
            print('swap {} {}'.format(i+1,j))
            return
    else:
        arr[j],arr[i]=arr[i],arr[j]
        if isSorted(arr):
            print('yes')
            print('swap {} {}'.format(i+1,j+1))
            return
    
    #print(i,j)
    
    i=0
    arr=original
    while arr[i]<arr[i+1] and i<len(arr)-1:
        i+=1
    j=i
    while arr[j]>arr[j+1] and j<len(arr)-2:
        j+=1
    arr=arr[:i]+arr[i:j+1][::-1]+arr[j+1:]
    if isSorted(arr):
        print('yes')
        if j-i==1:
            print('swap {} {}'.format(i+1,j+1))
        else:
            print('reverse {} {}'.format(i+1,j+1))        
        return
    print('no')
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
