#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the theGreatXor function below.
def theGreatXor(x):
    return (1 << len(bin(x)[2:])) - (x + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
