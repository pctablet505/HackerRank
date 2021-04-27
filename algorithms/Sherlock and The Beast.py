#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the decentNumber function below.
def decentNumber(n):
    y = n
    while y % 3 != 0:
        y -= 5
        if y < 0:
            break
    return y * '5' + (n - y) * '3' if y >= 0 else -1


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
