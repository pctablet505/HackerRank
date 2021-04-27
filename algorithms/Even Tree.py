#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import deque
from math import ceil, log2


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.subtree_weights = dict()
        self.parents = defaultdict(list)
        self.sums = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def getPath(self, start, end):
        if start == end:
            return [start]

        def util(parent, end):
            # print(parent)
            curr = end
            path = [end]
            while curr in parent:
                path.append(parent[curr])
                curr = parent[curr]
            return path

        visited = set()
        q = deque()
        q.appendleft(start)
        visited.add(start)
        parent = {}
        while len(q):
            v = q.pop()

            # print(v)
            for x in self.graph[v]:
                if x not in visited:
                    # path.append(x.vertex)
                    parent[x] = v
                    q.appendleft(x)
                    visited.add(x)
                    if x == end:
                        # parent[x.vertex]=v
                        return util(parent, end)

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
        self.root = 1
        self.parent = dict()
        self.parent[self.root] = None

        def DFS(self):
            stack = []
            visited = set()
            current = self.root
            visited.add(current)
            stack.append(current)
            while len(stack) > 0:
                v = stack.pop()

                for x in self.graph[v]:
                    if x not in visited:
                        stack.append(x)
                        visited.add(x)
                        self.parent[x] = v

        DFS(self)

    def assignSubtreeWeights(self):
        def util(self, u):
            for x in self.graph[u]:
                if x != u and x != self.parent[u]:
                    self.subtree_weights[u] += util(self, x)
            self.sums[self.subtree_weights[u]].append(u)
            return self.subtree_weights[u]

        util(self, self.root)


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    g = Graph()
    for i in range(t_edges):
        g.addEdge(t_from[i], t_to[i])
    for x in g.graph:
        g.subtree_weights[x] = 1
    g.getTree()
    g.assignSubtreeWeights()
    res = 0
    # print(g.subtree_weights)
    for x in g.subtree_weights:
        if x != 1 and g.subtree_weights[x] % 2 == 0:
            res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
