pacman=map(int,input().split())
food=map(int,input().split())
m,n=map(int,input().split())

matrix=[]

for i in range(m):
    matrix.append([x for x in input()])

explored=set()
moves=[(-1,0),(0,-1),(0,1),(1,0)][::-1]

arr=[]
flag=False
parent={}
parent[pacman]=None

def dfs(u):
    global flag
    if flag:
        return    
    arr.append(u)
    explored.add(u)
    i,j=u
    if u==food:
        flag=True
        return
    for x,y in moves:
        v=i+x,j+y
        if 0<=v[0]<m and 0<=v[1]<n:
            x,y=v
            if v not in explored and matrix[x][y] in '-.':
                parent[v]=u
                dfs(v)
    
dfs(pacman)
path=[]
x=food
while x!=None:
    path.append(x)
    x=parent[x]
path.reverse()

print(len(arr)):
for x,y in arr:
    print(x,y)
print(len(path)-1)
for x,y in path:
    print(x,y)
    
