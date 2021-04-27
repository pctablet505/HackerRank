#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the separateNumbers function below.
def separateNumbers(string):
    n = len(string)
    l = 1
    if n == 1:
        return 'NO'
    if n == 2:
        if int(string[0]) == int(string[1]) - 1:
            return 'TRUE ' + string[0]
        else:
            return 'NO'
    while l <= n / 2:
        lo = l
        i = 0

        prev = int(string[i:i + l])
        first = prev
        i += l
        if prev == 10 ** l - 1:
            l += 1

        if prev == 10 ** l - 1:
            l += 1
        while i < n:
            if string[i] == '0':
                break
            curr = int(string[i:i + l])
            if curr != prev + 1:
                break

            prev = curr
            i += l
            if prev == 10 ** l - 1:
                l += 1

        if i >= n:
            return 'YES ' + str(first)

        l = lo + 1
    return "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
