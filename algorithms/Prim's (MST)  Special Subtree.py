#!/bin/python3

import math
import os
import random
import re
import sys

"""
Created on Sun Mar 29 23:50:58 2020

@author: rahul
"""

from collections import defaultdict
from queue import deque


class MinHeapNode:
    def __init__(self, v, dist):
        self.dist = dist
        self.v = v


class Heap:
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = dict()

    def empty(self):
        return self.size == 0

    def swapMinHeapNode(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def minHeapify(self, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.size and self.array[l].dist < self.array[smallest].dist:
            smallest = l
        if r < self.size and self.array[r].dist < self.array[smallest].dist:
            smallest = r
        if smallest != i:
            self.pos[self.array[smallest].v] = i
            self.pos[self.array[i].v] = smallest
            self.swapMinHeapNode(smallest, i)
            self.minHeapify(smallest)

    def extractMin(self):
        if self.empty():
            return
        root = self.array[0]
        last = self.array[self.size - 1]
        self.array[0] = last
        self.pos[last.v] = 0
        self.pos[root.v] = self.size - 1
        self.size -= 1
        self.minHeapify(0)
        return root

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i].dist = dist
        while i > 0 and self.array[i].dist < self.array[(i - 1) // 2].dist:
            self.pos[self.array[i].v] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2].v] = i
            self.swapMinHeapNode(i, (i - 1) // 2)
            i = (i - 1) // 2

    def isInMinHeap(self, v):
        return self.pos[v] < self.size


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append(Node(v, w))
        self.graph[v].append(Node(u, w))

    def primMST(self, start):
        V = len(self.graph)
        key = dict().fromkeys(self.graph, float('inf'))
        parent = dict().fromkeys(self.graph, None)
        minHeap = Heap()
        i = 0
        for v in self.graph:
            minHeap.array.append(MinHeapNode(v, float('inf')))
            minHeap.pos[v] = i
            i += 1
        key[start] = 0
        minHeap.decreaseKey(start, 0)
        minHeap.size = V
        while not minHeap.empty():
            u = minHeap.extractMin().v
            for pCrawl in self.graph[u]:
                v = pCrawl.vertex
                if minHeap.isInMinHeap(v) and pCrawl.weight < key[v]:
                    key[v] = pCrawl.weight
                    parent[v] = u
                    minHeap.decreaseKey(v, key[v])
        result = 0
        for x in key:
            result += key[x]
        return result


def prims(n, edges, start):
    g = Graph()
    for e in edges:
        g.addEdge(e[0], e[1], e[2])
    return g.primMST(start)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
