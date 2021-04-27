#!/bin/python3

import os
import sys

import bisect
parents={}
rep={}
def make_set(n):
    global parents, rep
    parents=dict(zip(range(1,n+1),(range(1,n+1))))
    rep=dict(zip(range(1,n+1),({i} for i in range(1,n+1))))
def addEdge(x,y,paths,w):
    xr=find(x)
    yr=find(y)
    paths[w]+=len(rep[xr])*len(rep[yr])
    if xr==yr:
        return
    else:
        if len(rep[yr])<len(rep[xr]):
            parents[yr]=xr
            rep[xr].update(rep[yr])
            del rep[yr]
        else:
            parents[xr]=yr
            rep[yr].update(rep[xr])
            del rep[xr]
def find(x):
    if parents[x]!=x:
        parent=find(parents[x])
        parents[x]=parent
    return parents[x]




def solve(tree, queries):
    n=len(tree)+1
    tree.sort(key=lambda x:x[2])
    paths={0:0}
    weights=[0]
    prev=0
    make_set(n)
    for x,y, weight in tree:
        if weight!=prev:
            weights.append(weight)
            paths[weight]=paths[prev]
        addEdge(x,y,paths,weight)
        prev=weight
    for l, r in queries:
        wr=weights[bisect.bisect_right(weights,r)-1]
        wl=weights[bisect.bisect_right(weights,l-1)-1]
        yield paths[wr]-paths[wl]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
