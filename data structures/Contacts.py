#!/bin/python3

import os
import sys
from collections import Counter
#
# Complete the contacts function below.
#
def contacts(queries):
    res=[]
    c=Counter()
    for opp,pat in queries:
        if opp=='add':
            for i in range(1,len(pat)+1):
                c[pat[0:i]]+=1
        else:
            res.append(c[pat])
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
