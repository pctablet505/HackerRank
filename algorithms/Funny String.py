#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funnyString function below.
def funnyString(s):
    t = s[::-1]
    r1 = []
    r2 = []
    for i in range(len(s) - 1):
        r1.append(abs(ord(s[i]) - ord(s[i + 1])))
        r2.append(abs(ord(t[i]) - ord(t[i + 1])))
    print(r1, r2)
    for i in range(len(s) - 1):
        if r1[i] == r2[i]:
            continue
        else:
            return 'Not Funny'

    else:
        return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
