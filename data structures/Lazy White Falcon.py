import sys
sys.setrecursionlimit(999999)
from collections import defaultdict
from math import ceil, log2
class BinaryIndexedTree:

    def __init__(self, n):
        self.n=n       
        self.tree = [0 for j in range(n)]
        

    def update(self, index,val):
        while index<self.n:
            self.tree[index]+=val
            index=index|(index+1)

    def getSum_(self, index):
        sum_ = 0
        while index >= 0:
            sum_+=self.tree[index]
            index=(index&(index+1))-1
        return sum_
    def getSum(self,l,r):
        return self.getSum_(r)-self.getSum_(l-1)
        
    

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
    res=0
    while head[a]!=head[b]:
        if depth[head[a]]>depth[head[b]]:
            a,b=b,a
        res+=st.getSum(pos[head[b]],pos[b])
        b=parent[head[b]]
    if depth[a]>depth[b]:
        a,b=b,a
    res+=st.getSum(pos[a],pos[b])
    return res
def update(a,w):
    global arr
    p=pos[a]
    st.update(p,-arr[p])
    st.update(p,w)
    arr[p]=w

n,q=map(int,input().split())
for i in range(n-1):
    u,v=map(int,input().split())
    addEdge(u,v)
dfs(0)
decompose(0,0)
st=BinaryIndexedTree(len(pos))

s=''
arr=defaultdict(int)
for i in range(q):
    a,b,c=map(int, input().split())
    if a==1:
        update(b,c)
    else:
        p=query(b,c)        
        s+=str(p)+'\n'
print(s)



