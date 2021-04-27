# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:36:46 2020

@author: rahul
"""

from collections import defaultdict
from collections import deque
from math import ceil, log2
import bisect
import sys
sys.setrecursionlimit(999999)

from collections import defaultdict
from math import ceil, log2
class SegmentTree:
    def __init__(self,arr):
        h=ceil(log2(len(arr)))
        self.max_size=2*(2**h)-1
        self.arr=[0]*self.max_size
        self.n=len(arr)
    def getMid(self,start,end):
        return (start+end)//2
    def getMax(self,l,r):
        if l<0 or r>self.n-1 or l>r:
            print('invalid Input')
            return float('None')
        def util(self,seg_start,seg_end,query_start,query_end,index):
            if query_start<=seg_start and query_end>=seg_end:
                return self.arr[index]
            if seg_end<query_start or seg_start>query_end:
                return float('-inf')
            mid=self.getMid(seg_start,seg_end)
            return max(util(self,seg_start,mid,query_start,query_end,2*index+1),util(self,mid+1,seg_end,query_start,query_end,2*index+2))
        return util(self,0,self.n-1,l,r,0)
    def update(self,index,new_val):
        def util(self,seg_start,seg_end,index,new_val,seg_index):
            if index<seg_start or index>seg_end:
                return
            self.arr[seg_index]=new_val
            if seg_end!=seg_start:
                mid=self.getMid(seg_start,seg_end)
                util(self,seg_start,mid,index,new_val,2*seg_index+1)
                util(self,mid+1,seg_end,index,new_val,2*seg_index+2)
                self.arr[seg_index]=max(self.arr[2*seg_index+1],self.arr[2*seg_index+2])
        if index<0 or index>self.n-1:
            print('invalid input')
            return 
        util(self,0,self.n-1,index,new_val,0)


parent=defaultdict(lambda: None)
depth=defaultdict(int)
heavy=defaultdict(lambda: None)
head=dict()
pos=dict()
cur_pos=0
graph=defaultdict(list)
def addEdge(u,v):
    graph[u].append(v)
    graph[v].append(u)

visited=set()
def dfs(u):
    global cur_pos,head,pos,heavy,parent
    size=1
    max_c_size=0
    visited.add(u)
    for v in graph[u]:
        if u!=parent[v] and v not in visited:
            parent[v]=u
            depth[v]=depth[u]+1
            c_size=dfs(v)
            size+=c_size
            if c_size>max_c_size:
                max_c_size=c_size
                heavy[u]=v
    return size
            

def decompose(u,h):
    global cur_pos,head,pos,heavy,parent
    head[u]=h
    pos[u]=cur_pos
    cur_pos+=1
    if heavy[u]:
        decompose(heavy[u],h)
    for v in graph[u]:
        if v!=parent[u] and v!=heavy[u]:
            decompose(v,v)
def query(a,b):
    global cur_pos,head,pos,heavy,parent,st,depth
    res=float('-inf')
    while head[a]!=head[b]:
        if depth[head[a]]>depth[head[b]]:
            a,b=b,a
        curr_heavy_path_max=st.getMax(pos[head[b]],pos[b])
        res=max(res,curr_heavy_path_max)
        b=parent[head[b]]
    if depth[a]>depth[b]:
        a,b=b,a
    last_heavy_path_max=st.getMax(pos[a],pos[b])
    res=max(res,last_heavy_path_max)
    return res
def update(u,w):
    st.update(pos[u],w)
n,q=map(int,input().split())
for i in range(n-1):
    u,v=map(int,input().split())
    addEdge(u,v)
dfs(0)
decompose(0,0)
st=SegmentTree(pos)

s=[]

for i in range(q):
    a,b,c=map(int, input().split())
    if a==1:
        update(b,c)
    else:
        p=query(b,c)        
        s.append(p)
for x in s:
    print(x)

