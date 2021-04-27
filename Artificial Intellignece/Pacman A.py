# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:57:56 2020

@author: rahul
"""

from collections import defaultdict,deque
import heapq

pacman=tuple(map(int,input().split()))
food=tuple(map(int,input().split()))
m,n=map(int,input().split())

matrix=[]

for i in range(m):
    matrix.append([x for x in input()])



visited=set()
moves=[(-1,0),(0,-1),(0,1),(1,0)]

flag=False
parent=defaultdict(lambda :None)
parent[pacman]=None

heap=[]
mappings=defaultdict(list)


def approximate(u):
    return abs(food[0]-u[0])+abs(food[1]-u[1])
dis_pacman=approximate(pacman)
mappings[dis_pacman].append(pacman)
heapq.heappush(heap,dis_pacman)
dist=defaultdict(lambda:0)

while heap:
    if flag:
        break   
    x=heapq.heappop(heap)
    u=mappings[x].pop()
    i,j=u
    if u==food:
        flag=True
        break
    for x,y in moves:
        v=i+x,j+y
        if 0<=v[0]<m and 0<=v[1]<n:
            x,y=v
            if v not in visited and matrix[x][y] in '-.':
                parent[v]=u
                dis=approximate(v)+dist[u]+1
                dist[v]=dist[u]+1
                mappings[dis].append(v)
                heapq.heappush(heap,dis)
                visited.add(v)
    
    

path=[]
x=food
while x!=None:
    path.append(x)
    x=parent[x]
path.reverse()

print(len(path)-1)
for x,y in path:
    print(x,y)
    
