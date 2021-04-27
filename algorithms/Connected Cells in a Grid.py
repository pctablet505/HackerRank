#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict,deque

def pointer(i,j,m,n):
    return (i)*n+j
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self,start,visited):
        count=1
        visited.add(start)
        for v in self.graph[start]:
            if v not in visited:
                count+=self.dfs(v,visited)
        return count



def maxRegion(grid):
    m=len(grid)
    n=len(grid[0])
    g=Graph()
    nodes=set()
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                u=pointer(i,j,m,n)
                nodes.add(u)
                if i<m-1 and grid[i+1][j]:
                    v=pointer(i+1,j,m,n)
                    g.addEdge(u,v)                    
                    nodes.add(v)
                if j<n-1 and grid[i][j+1]:
                    v=pointer(i,j+1,m,n)
                    g.addEdge(u,v)                    
                    nodes.add(v)
                if i<m-1 and j<n-1 and grid[i+1][j+1]:
                    v=pointer(i+1,j+1,m,n)
                    g.addEdge(u,v)
                    nodes.add(v)
                    
                if i<m-1 and j>0 and grid[i+1][j-1]:
                    v=pointer(i+1,j-1,m,n)
                    g.addEdge(u,v)
                    nodes.add(v)
    visited=set()
    res=0
    for u in nodes:
        if u not in visited:
            res=max(res,g.dfs(u,visited))
        
    
    return res    

            
                




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
