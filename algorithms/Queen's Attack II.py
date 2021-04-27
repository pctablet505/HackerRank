#!/bin/python3

import math
import os
import random
import re
import sys


def moveQ(n, ur, uc, r, c, obstacles):
    p = 0
    while True:
        r = ur + r
        c = uc + c
        key = (r - 1) * n + c
        if c < 1 or r < 1 or c > n or r > n or key in obstacles:
            return p
        p += 1
    return p


def queensAttack(n, k, r_q, c_q, obstacles):
    obs = dict()
    for b in obstacles:
        obs[(b[0] - 1) * n + b[1]] = True
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 1, 0]
    res = 0
    for i in range(8):
        res += moveQ(n, dr[i], dc[i], r_q, c_q, obs)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
