#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    p=r'[.]*[h]{1,}(.)*[a]{1,}(.)*[c]{1,}(.)*[k]{1,}(.)*[e]{1,}(.)*[r]{1,}(.)*[r]{1,}(.)*[a]{1,}(.)*[n]{1,}(.)*[k]{1,}(.)*'
    if re.findall(p,s):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
