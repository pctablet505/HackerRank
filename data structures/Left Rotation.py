#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    temp = []
    for i in range(d):
        temp.append(a[i])
    for i in range(n - d):
        a[i] = a[i + d]
    for i in range(d):
        a[i + n - d] = temp[i]
    for x in a:
        print(x, end=' ')
