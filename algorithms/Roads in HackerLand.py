#!/bin/python3

import os
import sys

#
# Complete the roadsInHackerland function below.
from collections import defaultdict
from queue import deque


class DisjointSet:
    def __init__(self, vertices):
        self.rank = dict().fromkeys(vertices, 1)
        self.parent = dict.fromkeys(vertices)
        for x in self.parent:
            self.parent[x] = x

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[x] = yset
        elif self.rank[yset] < self.rank[xset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


result = 0


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(set)
        self.count = defaultdict(int)

    def addEdge(self, u, v, w):
        self.graph[u].add((v, w))
        self.graph[v].add((u, w))

    def dfs(self, src, parent=-1):
        global n, result
        no_children = 0
        for v, w in self.graph[src]:
            if v != parent:
                children = self.dfs(v, src)
                k = (n - children) * children
                result += k * (1 << w)
                no_children += children
        return no_children + 1

    def kruskalsMST(self, edges):
        edges.sort(key=lambda x: x[2])
        vertices = set()
        for u, v, w in edges:
            vertices.add(u)
            vertices.add(v)
        disjoit = DisjointSet(vertices)
        result = []
        i = 0
        e = 0
        while e < len(vertices) - 1:
            u, v, w = edges[i]
            i += 1
            x = disjoit.find(u)
            y = disjoit.find(v)
            if x != y:
                e += 1
                result.append((u, v, w))
                disjoit.union(x, y)
        self.vertices = vertices
        return result


def roadsInHackerland(n, roads):
    global result
    g = Graph()
    tree = g.kruskalsMST(roads)
    for u, v, w in tree:
        g.addEdge(u, v, w)
    g.dfs(1)
    return bin(result)[2:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    fptr.write(result + '\n')

    fptr.close()
