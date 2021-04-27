#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort,bisect_right

# Complete the maximumSum function below.
def maximumSum(arr,n,m):
    
    prefix=[0]*n
    curr=0
    for i in range(n):
        curr=(arr[i]%m+curr)%m
        prefix[i]=curr
    pq=[prefix[0]]
    max_sum=max(prefix)
    for i in range(1,n):
        left=bisect_right(pq,prefix[i])
        if left!=len(pq):
            modsum=(prefix[i]-pq[left]+m)%m
            max_sum=max(modsum,max_sum)
        insort(pq,prefix[i])
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a,n,m)

        fptr.write(str(result) + '\n')

    fptr.close()
