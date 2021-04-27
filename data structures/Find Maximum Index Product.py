#!/bin/python3

import os
import sys

sys.setrecursionlimit(9999999)


class Node:
    def __init__(self, v, i):
        self.v = v
        self.i = i
        self.left = None
        self.right = None


def insert(x, t):
    if not t:
        t = x
    elif t.v == x.v:
        t.i = x.i
    else:
        x.left, x.right = split(t, x.v)
        t = x
    return t


def split(p, val):
    if not p:
        return (None, None)
    elif p.v > val:
        l, p.left = split(p.left, val)
        r = p
    else:
        p.right, r = split(p.right, val)
        l = p
    return (l, r)


def solve(arr):
    n = len(arr)
    l = [0] * n
    r = [0] * n
    tL = None
    tR = None
    i = 0
    j = n - 1
    while i < n:
        tL = insert(Node(arr[i], i + 1), tL)
        tR = insert(Node(arr[j], j + 1), tR)
        l[i] = tL.right.i if tL.right else 0
        r[j] = tR.right.i if tR.right else 0
        i += 1
        j -= 1
    ans = float('-inf')
    for i in range(n):
        ans = max(ans, l[i] * r[i])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
