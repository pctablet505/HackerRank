#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    s = set()
    res = []
    for i in range(1, n + 1):
        if (i - k > 0 and (i - k) and i - k <= n and i - k not in s) and (
                i + k > 0 and i + k <= n and (i + k) not in s):

            x = min(i + k, i - k)
            res.append(x)
            print(x, s.add(x))
            continue
        elif i + k > 0 and (i + k) not in s and i + k <= n:
            s.add(i + k)
            res.append(i + k)
            continue
        elif (i - k > 0 and (i - k) not in s and i - k <= n):
            s.add(i - k)
            res.append(i - k)
        else:
            return [-1]
    else:
        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
