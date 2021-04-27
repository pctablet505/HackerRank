#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):
    count = 0
    if len(s) > 0:
        count += 1
    for x in s:

        if x.isupper():
            print(x)

            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
