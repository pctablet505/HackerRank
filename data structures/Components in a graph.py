#!/bin/python3

import os
import sys
from collections import defaultdict
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFSUtil(self, s, visited):
        a = []
        q = queue.Queue()
        q.put_nowait(s)
        visited[s] = True
        while not q.empty():
            s = q.get_nowait()
            a.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    q.put_nowait(i)
                    visited[i] = True
        return a

    def BFS(self):
        x = []
        M = 0
        m = float('inf')
        V = len(self.graph)
        visited = dict().fromkeys(self.graph, False)
        for i in visited:
            if not visited[i]:
                b = self.BFSUtil(i, visited)
                l = len(b)
                M = max(l, M)
                if l > 1:
                    m = min(m, l)
        return [m, M]


def componentsInGraph(gb):
    g = Graph()
    for x in gb:
        g.addEdge(x[0], x[1])
    result = g.BFS()
    return result

    #
    # Write your code here.
    #


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
