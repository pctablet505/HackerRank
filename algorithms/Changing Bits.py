#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#
'''set_a 0 1

get_c 5

get_c 1

set_b 2 0

get_c 5'''


def changeBits(a, b, queries):
    a = int(a, 2)
    b = int(b, 2)
    s = ''
    for q in queries:
        q = q.split()
        if q[0] == 'set_a':
            ind = int(q[1])
            val = q[2]
            left = a >> (ind + 1)
            right = a & ((1 << ind) - 1)
            a = left << (ind + 1)
            a |= int(val) << ind
            a |= right
        elif q[0] == 'set_b':
            ind = int(q[1])
            val = q[2]
            left = b >> (ind + 1)
            right = b & ((1 << ind) - 1)
            b = left << (ind + 1)
            b |= int(val) << ind
            b |= right
        elif q[0] == 'get_c':
            ind = int(q[1])
            # print(a,b,a+b,ind)
            print(((a + b) >> ind) & 1, end='')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])

    queries_size = int(first_multiple_input[1])

    a = input()

    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
