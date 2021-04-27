#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    from queue import deque
    s = [int(x) for x in s]
    q = set()
    mid = []
    if n & 1:
        left = s[:n // 2]
        right = s[n // 2 + 1:][::-1]
        mid = [s[n // 2]]
    else:
        left = s[:n // 2]
        right = s[n // 2:][::-1]
    for i in range(len(left)):
        if left[i] == right[i]:
            continue
        elif k > 0:
            m = max(left[i], right[i])
            left[i] = right[i] = m
            q.add(i)
            k -= 1
        else:
            return '-1'

    for i in range(len(left)):
        if left[i] == right[i] == 9:
            continue
        elif k > 0 and left[i] != 9 and right[i] == 9:
            left[i] = right[i] = 9
            k -= 1
        elif k > 0 and left[i] == 9 and right[i] != 9:
            left[i] = right[i] = 9
            k -= 1
        else:
            if i in q and k > 0:
                left[i] = right[i] = 9
                k -= 1
            elif k > 1:
                left[i] = right[i] = 9
                k -= 2
        if k < 1:
            break

    if mid and k:
        if mid[0] != 9:
            mid[0] = 9
            k -= 1
    return ''.join([str(x) for x in left + mid + right[::-1]])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
