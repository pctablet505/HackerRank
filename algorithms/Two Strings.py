#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    d1 = dict().fromkeys(letters, 0)
    d2 = dict().fromkeys(letters, 0)
    for x in s1:
        d1[x] += 1
    for x in s2:
        d2[x] += 1
    for x in letters:
        if d1[x] and d2[x]:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
