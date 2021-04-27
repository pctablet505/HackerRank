#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

parent = dict()
machines = defaultdict(bool)
size = dict()


def find(x):
    if parent[x] == x:
        return (x, machines[x])
    parent[x], machines[x] = find(parent[x])
    return (parent[x], machines[x])


def merge(a, b, f=False):
    a, fa = find(a)
    b, fb = find(b)
    if a == b:
        return
    if size[b] < size[a]:
        a, b = b, a
    parent[b] = a
    if f:
        machines[a] = True
        machines[b] = True
    size[a] += size[b]


def minTime(roads, machines_node):
    machines_node = set(machines_node)
    roads.sort(key=lambda x: x[2], reverse=True)
    result = 0
    for u, v, w in roads:
        if u not in parent:
            parent[u] = u
            size[u] = 1
            if u in machines_node:
                machines[u] = True
        if v not in parent:
            parent[v] = v
            size[v] = 1
            if v in machines_node:
                machines[v] = True
        pu, mu = find(u)
        pv, mv = find(v)

        if mu and mv:
            result += w
        else:
            merge(pu, pv, mu | mv)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machine = []

    for _ in range(k):
        machines_item = int(input())
        machine.append(machines_item)

    result = minTime(roads, machine)

    fptr.write(str(result) + '\n')

    fptr.close()
