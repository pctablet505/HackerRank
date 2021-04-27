#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the findDigits function below.
def findDigits(n):
    count = 0
    digits = Counter(map(int, [x for x in str(n)]))
    for x in digits:
        if x != 0 and n % x == 0:
            count += digits[x]
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
