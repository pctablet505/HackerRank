#!/bin/python3

import math
import os
import random
import re
import sys


from collections import defaultdict
from queue import deque

    
                                                             
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def BFS(self,start,n):
        dist=dict().fromkeys(range(1,n+1),-1)        
        visited=dict().fromkeys(self.graph,False)
        dist=dict().fromkeys(range(1,n+1),-1)
        q=deque()
        q.append((start,0))
        while q:
            v,curr_cost=q.popleft()            
            
            for x in self.graph[v]:
                if not visited[x]:
                    visited[x]=True
                    dist[x]=curr_cost+6
                    q.append((x,dist[x]))
        result=[]
        for i in range(1,n+1):
            if i!=start:
                result.append(dist[i])
        return result
        
        
        

def bfs(n, m, edges, s):
    g=Graph()
    for x in edges:
        g.addEdge(x[0],x[1])
    return g.BFS(s,n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
