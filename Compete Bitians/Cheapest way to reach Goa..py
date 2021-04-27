import sys
sys.setrecursionlimit(999999)
from collections import defaultdict
from queue import deque
class MinHeapNode:
    def __init__(self,v,dist):
        self.dist=dist
        self.v=v
class Heap:
    def __init__(self):
        self.array=[]
        self.size=0
        self.pos=dict()
    def empty(self):
        return self.size==0
    def swapMinHeapNode(self,a,b):
        self.array[a],self.array[b]=self.array[b],self.array[a]
    def minHeapify(self,i):
        smallest=i
        l=2*i+1
        r=2*i+2
        if l<self.size and self.array[l].dist<self.array[smallest].dist:
            smallest=l
        if r<self.size and self.array[r].dist<self.array[smallest].dist:
            smallest=r
        if smallest!=i:
            self.pos[self.array[smallest].v]=i
            self.pos[self.array[i].v]=smallest
            self.swapMinHeapNode(smallest,i)
            self.minHeapify(smallest)
    def extractMin(self):
        if self.empty():
            return 
        root=self.array[0]
        last=self.array[self.size-1]
        self.array[0]=last
        self.pos[last.v]=0
        self.pos[root.v]=self.size-1
        self.size-=1
        self.minHeapify(0)
        return root
    def decreaseKey(self,v,dist):
        i=self.pos[v]
        self.array[i].dist=dist
        while i>0 and self.array[i].dist<self.array[(i-1)//2].dist:
            self.pos[self.array[i].v]=(i-1)//2
            self.pos[self.array[(i-1)//2].v]=i
            self.swapMinHeapNode(i,(i-1)//2)
            i=(i-1)//2
    def isInMinHeap(self,v):
        return self.pos[v]<self.size
    
                                                             
class Node:
    def __init__(self,vertex,weight):
        self.vertex=vertex
        self.weight=weight
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v,w):
        self.graph[u].append(Node(v,w))
        self.graph[v].append(Node(u,w))
    def DFS(self):
        stack=deque()
        visited=dict().fromkeys(self.graph,False)
        current=next(iter(self.graph))
        visited[current]=True
        stack.append(current)
        while len(stack)>0:
            v=stack.pop()
            print(v)
            visited[v]=True
            for x in self.graph[v]:
                if not visited[x.vertex]:
                    stack.append(x.vertex)
    def dijkstra(self,src):
        V=len(self.graph)
        dist=dict().fromkeys(self.graph,float('inf'))
        heap=Heap()
        i=0
        for v in self.graph:
            heap.array.append(MinHeapNode(v,float('inf')))
            heap.pos[v]=i
            i+=1
        dist[src]=0
        heap.decreaseKey(src,dist[src])
        heap.size=V
        while not heap.empty():
            u=heap.extractMin().v
            for pCrawl in self.graph[u]:
                v=pCrawl.vertex
                if heap.isInMinHeap(v) and dist[u]!=float('inf') and pCrawl.weight+dist[u]<dist[v]:
                    dist[v]=pCrawl.weight+dist[u]
                    heap.decreaseKey(v,dist[v])
        return dist
        
g=Graph()
initial=int(input())
n,m=map(int,input().split())
for i in range(n):
    g.graph[i]
for _ in range(m):
    u,v,w=map(int,input().split())
    g.addEdge( u, v, w)
d=g.dijkstra(0)[n-1]
if d==float('inf') or initial-d<0:
    print(-1)
else:
    print(initial-d)