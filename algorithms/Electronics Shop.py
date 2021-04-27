#!/bin/python3

import os
import sys
from itertools import combinations as cb


def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    price = []
    for x in keyboards:
        for y in drives:
            if x < b and y < b:
                sum = x + y
                if sum <= b:
                    price.append(sum)
    if price == []:
        return -1
    return max(price)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
