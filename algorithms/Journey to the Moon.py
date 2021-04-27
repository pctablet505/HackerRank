#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

C = [[0 for _ in range(10000)] for _ in range(10)]


def nCr(n, r):
    global C
    if C[n][r]:
        return C[n][r]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][r]


class Graph:
    def __init__(self, ):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, visited, vertex):
        i = 0
        stack = []
        visited.add(vertex)
        stack.append(vertex)
        while stack:
            v = stack.pop()
            i += 1
            for x in self.graph[v]:
                if x not in visited:
                    stack.append(x)
                    visited.add(x)
        return i

    def DFS(self):
        result = []
        visited = set()
        for x in self.graph:
            if x not in visited:
                result.append(self.DFSUtil(visited, x))
        return result


def journeyToMoon(n, astronaut):
    g = Graph()
    for i in range(n):
        g.addEdge(i, i)
    for u, v in astronaut:
        g.addEdge(u, v)
    counts = g.DFS()

    s = 0
    res = 0
    for x in counts:
        res += x * s
        s += x
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
