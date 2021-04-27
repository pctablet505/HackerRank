#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countLuck function below.
def countLuck(matrix, k):
    from queue import Queue
    m=len(matrix)
    n=len(matrix[0])
    start=None
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=='M':
                start=(i,j)
                break
    stack=[start]
    visited=set()
    flag=True
    parent=dict()
    counts=dict()
    parent[start]=None
    while stack and flag:

        u=stack.pop()
        visited.add(u)
        i,j=u
        c=0
        for v in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
            if v not in visited:
                a,b=v
                if 0<=a<m and 0<=b<n and matrix[a][b]!='X':
                    c+=1
                    parent[v]=u
                    stack.append(v)
                    if matrix[a][b]=='*':
                        target=v
                        flag=False
        counts[u]=c
    count=0
    target=parent[target]
    while target:        
        if counts[target]>1:
            count+=1
        target=parent[target]
    
    if count==k:
        return 'Impressed'
    return 'Oops!'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
