#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


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


def roadsAndLibraries(n, c_lib, c_road, cities):
    g = Graph()
    for i in range(1, n + 1):
        g.addEdge(i, i)
    for u, v in cities:
        g.addEdge(u, v)
    counts = g.DFS()
    print(counts)
    amt = 0
    if c_lib < c_road:
        amt = sum(counts) * c_lib
    else:
        for num in counts:
            if num > 1:
                amt += c_lib + (num - 1) * c_road
            else:
                amt += c_lib
    return amt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
