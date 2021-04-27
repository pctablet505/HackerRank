#!/bin/python3

import math
import os
import random
import re
import sys

arr = []


def median():
    size = len(arr)
    if size % 2 == 0:
        m = (arr[size // 2 - 1] + arr[size // 2]) / 2
        return m
    else:
        m = (arr[(size - 1) // 2])
        return m


def remove(l,r,x):
    if l>r:
        return False
    else:
        m=(l+r+1)//2
        if arr[m]==x:
            del arr[m]
            return True
        elif arr[m]<x:
            return remove(m+1,r,x)
        else:
            return remove(l,m-1,x)


def insert(l, r, x):
    if l == r:
        arr.insert(r, x)
    else:
        m = (l + r) // 2
        if arr[m] == x:
            arr.insert(m, x)
        elif arr[m] < x:
            insert(m + 1, r, x)
        else:
            insert(l, m, x)


def activityNotifications(expenditure, d):
    global arr
    n = len(expenditure)

    if d >= n:
        return 0
    c = 0
    for i in range(d):
        if not arr:
            arr += [expenditure[i]]
        else:
            insert(0, len(arr), expenditure[i])

    for i in range(d, n):
        if 2 * median() <= expenditure[i]:
            c += 1
        remove(0, len(arr),expenditure[i-d])
        insert(0, len(arr), expenditure[i])
    return c


if __name__ == '__main__':


    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

