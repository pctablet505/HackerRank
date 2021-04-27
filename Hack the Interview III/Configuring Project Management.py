#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        for i in range(1, vertices + 1):
            self.graph[i]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def solve(self, n):
        res = set()
        if n < 3:
            return [-1]
        f2 = set()
        f2.add(2)
        visited = [False] * (n + 1)
        for x in self.graph[2]:
            if x != 1 and not visited[x]:
                f2.add(x)
                visited[x] = True
                for y in self.graph[x]:
                    if y != 1 and not visited[y]:
                        f2.add(y)
                        visited[y] = True

        for x in self.graph[1]:
            if x not in f2:
                res.add(x)

        if res:
            return sorted(res)
        return [-1]


def configureProjectPresentation(n, friendships):
    g = Graph(n)
    for u, v in friendships:
        if u != v:
            g.addEdge(u, v)
    return g.solve(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        freiendships = []

        for _ in range(m):
            freiendships.append(list(map(int, input().rstrip().split())))

        result = configureProjectPresentation(n, freiendships)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
