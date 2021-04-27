#!/bin/python3

import os
import sys
from collections import defaultdict
import queue
class Graph:
    def __init__(self):
        self.graph=defaultdict(set)
    def addEdge(self,u,v):
        self.graph[u].add(v)
        self.graph[v].add(u)
    def DFS(self,n,s):
        q=queue.Queue()
        dist=dict()
        remaining=set([i for i in range(1,n+1)])
        q.put((s,0))
        visited=set()
        visited.add(s)
        remaining.discard(s)
        while not q.empty() and remaining:
            u,d=q.get()
            
            to_disc=[]
            for v in remaining:
                if v not in visited and v not in self.graph[u]:
                    dist[v]=d+1
                    q.put((v,d+1))
                    to_disc.append(v)
            for k in to_disc:
                remaining.discard(k)
            
        result=[]
        for i in range(1,n+1):
            if i!=s:
                result.append(dist[i])
        return result


def rustMurderer(n, roads,s):
    g=Graph()
    for u,v in roads:
        g.addEdge(u,v)
    
    return g.DFS(n,s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads,s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
