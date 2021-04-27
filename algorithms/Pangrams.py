#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    c = Counter([x for x in s])
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if not i in c:
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
