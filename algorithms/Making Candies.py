#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    stock=0
    upgrade=0
    spend=float('inf')
    while stock<n:
        passes=(p-stock)//(m*w)
        if passes<=0:
            production=(stock//p)+m+w
            half=math.ceil(production/2)
            if m>w:
                m=max(m,half)
                w=production-m
            else:
                w=max(w,half)
                m=production-w
            stock%=p
            passes=1
        stock+=passes*m*w
        upgrade+=passes
        spend=min(spend,upgrade+math.ceil((n-stock)/(m*w)))
    return min(upgrade,spend)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
