#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    dp=[0]*(k+1)
    for i in range(k+1):
        for j in range(n):
            if arr[j]<=i:
                dp[i]=max(dp[i],dp[i-arr[j]]+arr[j])
    return dp[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for _ in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        arr = list(map(int, input().rstrip().split()))
        result = unboundedKnapsack(k, arr)
        fptr.write(str(result) + '\n')

    fptr.close()
