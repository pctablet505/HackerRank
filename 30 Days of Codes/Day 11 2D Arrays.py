#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    M = float('-inf')
    for i in range(4):
        for j in range(4):
            s = 0
            for k in range(3):
                s += sum(arr[i + k][j:j + 3])

            s -= arr[i + 1][j] + arr[i + 1][j + 2]

            M = max(M, s)
    print(M)
