#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(999999)

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
from collections import defaultdict
from collections import deque
from math import ceil,log2



class Graph:
    def __init__(self):
        self.graph = defaultdict(list)        
        self.subtree_weights=dict()        
        self.parents=defaultdict(list)
        self.depth=defaultdict(int)
        
        
        
        

    def addEdge(self, u, v):
        self.graph[u].append(v)        
        self.graph[v].append(u)

    def DFS(self, start=None):
        stack = []
        visited = set()
        if not start:
            current = next(iter(self.graph))
        else:
            current = start
        visited.add(current)
        stack.append(current)
        while len(stack) > 0:
            v = stack.pop()
            
            print(v)
            for x in self.graph[v]:
                if x not in visited:
                    stack.append(x)
                    visited.add(x)                    
            
    def getPath(self, start,end):
        if start==end:
            return [start]        
        def util(parent,end):
            #print(parent)
            curr=end
            path=[end]
            while curr in parent:
                path.append(parent[curr])
                curr=parent[curr]
            return path
        
        
        visited = set()
        q = deque()
        q.appendleft(start)
        visited.add(start)
        parent={}
        while len(q):
            v = q.pop()
            
            #print(v)
            for x in self.graph[v]:
                if x not in  visited:
                    #path.append(x.vertex)
                    parent[x]=v
                    q.appendleft(x)
                    visited.add(x)
                    if x==end:
                        #parent[x.vertex]=v
                        return util(parent,end)


    def longestPahInTree(self):
        start = next(iter(self.graph))
        def util(self, start):
            farthest = start
            visited = set()
            q = deque()
            q.appendleft(start)
            visited.add(start)
            while len(q):
                v = q.pop()

                for x in self.graph[v]:
                    if x not in visited:
                        farthest = x
                        q.appendleft(x)
                        visited.add(x)
            return farthest

        d1 = util(self, start)
        d2 = util(self, d1)
        return d1, d2

    def getTreeRoot(self):
        start, end = self.longestPahInTree()
        path = self.getPath(start, end)
        root = path[len(path) // 2]
        return root

    def getTree(self):
        self.root = self.getTreeRoot()
        
        self.parent = dict()
        self.parent[self.root] = None
        

        def DFS(self):
            stack = []
            visited = set()
            current = self.root
            self.depth[current]=1
            visited.add(current)
            stack.append(current)            
            while len(stack) > 0:
                v = stack.pop()  
                
                for x in self.graph[v]:    
                    if x not in visited:
                        stack.append(x)
                        visited.add(x)
                        self.parent[x] = v
                        
                        self.depth[x]=self.depth[v]+1
        DFS(self)
        
    def isAncestor(self,u,v):
        return self.enter[u]<=self.enter[v] and self.exit[v]<=self.exit[u]

    def getTreePath(self, u, v):
        p1 = []
        p2 = []
        lca=self.LCA(u, v)
        a=u
        b=v       
        while a!=lca:            
            p1.append(a)
            if a==v:
                return p1
            a = self.parent[a]
        p1.append(a)
        while b!=lca:
           
            p2.append(b)
            if b==u:
                return p2
            b = self.parent[b]
                

        return p1 + p2[::-1]
    
    
    def assignSubtreeWeights(self):        
        
        def util(self,u):            
            for x in self.graph[u]:                
                if x !=u and x!=self.parent[u]:
                    self.subtree_weights[u]+=util(self,x)
            return self.subtree_weights[u]
        util(self,self.root)

def solve(g,total):
    ans=float('inf')
    visited=set()
    stack=[g.root]
    while stack:
        u=stack.pop()
        visited.add(u)
        for v in g.graph[u]:
            if v not in visited and v!=g.parent[u]:
                a=g.subtree_weights[v]
                b=total-a
                diff=abs(a-b)
                ans=min(ans,diff)
                stack.append(v)
    return ans
def cutTheTree(data, edges):
    g=Graph()
    for u,v in edges:
        g.addEdge(u,v)
    for i in range(len(data)):
        g.subtree_weights[i+1]=data[i]
    g.getTree()
    g.assignSubtreeWeights()
    return solve(g,sum(data))
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
