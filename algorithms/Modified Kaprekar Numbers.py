#!/bin/python3

import math
import os
import random
import re
import sys


def isKarpekar(n):
    x = n ** 2
    d = str(x)
    l = len(d)
    if l < 2:
        return n == x
    m = l // 2
    # print(m)
    # print(d[:m],d[m:])
    '''
    if l&1:        
        if int(d[:m+1])+int(d[m+1:])==n:
            return True
    '''
    if int(d[:m]) + int(d[m:]) == n:
        return True
    return False


def kaprekarNumbers(p, q):
    s = ''
    for x in range(p, q + 1):
        if isKarpekar(x):
            s += str(x) + ' '
    s = s.strip()
    if s:
        print(s)
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
