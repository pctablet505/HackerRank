#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    c = Counter([x for x in s])
    distinct_counts = set(c.values())

    if len(distinct_counts) > 2:
        return 'NO'
    if len(distinct_counts) == 1:
        return 'YES'
    a, b = sorted(distinct_counts)
    print(a,b)
    ca = 0
    cb = 0
    for x in c:
        if c[x] == a:
            ca += 1
        else:
            cb += 1
    ca, cb = ([ca, cb])
    if a==1 and ca>1:
        return 'NO'
    if b==1 and cb>1:
        return 'NO'
    if ca==1 and a-b>1 or cb==1 and b-a>1:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
