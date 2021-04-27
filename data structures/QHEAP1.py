from heapq import heappush, heappop
arr=[]
items=set()
if __name__=='__main__':
    for _ in range(int(input())):
        inp=list(map(int,input().split()))
        if inp[0]==1:
            heappush(arr,inp[1])
            items.add(inp[1])
        if inp[0]==2:
            items.discard(inp[1])
        if inp[0]==3:
            while arr[0] not in items:
                heappop(arr)
            print(arr[0])
