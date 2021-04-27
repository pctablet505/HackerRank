#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jimOrders function below.
def jimOrders(orders):
    result = []
    for x in range(len(orders)):
        result.append([x + 1, orders[x][0] + orders[x][1]])
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    # print(result)
    return list(map(lambda x: x[0], result))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
