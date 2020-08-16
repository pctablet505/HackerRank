def heapifyMin(arr,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[smallest]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest=r
    if smallest != i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapifyMin(arr,n,smallest)
def shiftUp(arr,i):
    if i==0:
        return
    parent=(i-1)//2
    if arr[i]<arr[parent]:
        arr[parent],arr[i]=arr[i],arr[parent]
        shiftUp(arr,parent)
def insert(arr,item):
    if len(arr)==0:
        arr.append(item)
    else:
        arr.append(item)
        shiftUp(arr,len(arr)-1)
    items.add(item)
def pop(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    arr.pop()
    n=len(arr)
    heapifyMin(arr,n,0)
arr=[]
items=set()
def get_min(arr,items):
    while arr[0] not in items:
        pop(arr)
    print(arr[0])


if __name__=='__main__':
    for _ in range(int(input())):
        inp=list(map(int,input().split()))
        if inp[0]==1:
            insert(arr,inp[1])
        if inp[0]==2:
            items.discard(inp[1])
        if inp[0]==3:
            get_min(arr,items)







    





        

