#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    c = Counter([x for x in s])
    e = 0
    o = 0
    for x in c:
        if c[x] & 1:
            o += 1
        else:
            e += 1
    if o > 1:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
