#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    print(grid)
    matrix=[[x for x in y] for y in grid]
    sizes=[]
    m=len(grid)
    n=len(grid[0])
    for i in range(m):
        for j in range(n):
            k=0
            if matrix[i][j]=='G':
                while i-k>=0 and i+k<m and j-k>=0 and k+j<n:
                    if matrix[i+k][j]==matrix[i-k][j]==matrix[i][j-k]==matrix[i][j+k]=='G':
                        k+=1
                        sizes.append((i,j,k))

                        continue
                    break
                    
            
            
    def modify(i,j,s):
        for a in range(s):
            matrix[i+a][j]=matrix[i-a][j]=matrix[i][j+a]=matrix[i][j-a]='B'
    def reverse(i,j,s):
        for a in range(s):
            matrix[i+a][j]=matrix[i-a][j]=matrix[i][j+a]=matrix[i][j-a]='G'
    def check(i,j,s):
        k=0
        for a in range(s):
            if matrix[i+a][j]==matrix[i-a][j]==matrix[i][j+a]==matrix[i][j-a]=='G':
                k+=1
            else:
                break
        return k
    
    sizes.sort(key=lambda x:(x[2]*4)-3)
    M=0
    
    for x in sizes:
        for y in sizes:                
            i1,j1,k1=x
            i2,j2,k2=y              
            modify(i1,j1,k1)                
            k2= check(i2,j2,k2)                    
            M=max(M,(k1*4-3)*(k2*4-3))
            reverse(i1,j1,k1)
    return M
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
