#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    transpose = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            transpose[j][i] = container[i][j]
    h = [sum(x) for x in container]
    v = [sum(x) for x in transpose]
    h.sort()
    v.sort()
    if h == v:
        return 'Possible'
    return 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
