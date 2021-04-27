#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sansaXor function below.
def sansaXor(arr):
    if len(arr) & 1:
        ans = arr[0]
        for i in range(2, len(arr), 2):
            ans ^= arr[i]
        return ans

    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
