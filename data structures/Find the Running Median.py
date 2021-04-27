import heapq
import os

'''
def heapifyDown(arr,i):
    largest=i
    l=2*i+1
    r=2*i+2
    n=len(arr)
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapifyDown(arr, largest)    
def heqpifyUp(arr,i):
    if i!=0:
        parent=(i-1)//2
        if arr[i]>arr[parent]:
            arr[i],arr[parent]=arr[parent],arr[i]
            heqpifyUp(arr,parent)
def insertMax(arr,item):
    arr.append(item)
    heqpifyUp(arr,len(arr)-1)
def pop(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    result=arr.pop()
    heapifyDown(arr, 0)
    return result
'''


def getBalance(x, y):
    return len(x) - len(y)


def runningMedian(a):
    maxH = []
    minH = []
    result = []
    for x in a:
        if not maxH or x <= maxH[0]:
            maxH.append(x)
            heapq._siftdown_max(maxH, 0, len(maxH) - 1)
        else:
            heapq.heappush(minH, x)

        if getBalance(maxH, minH) > 1:
            heapq.heappush(minH, heapq._heappop_max(maxH))
        if getBalance(maxH, minH) < -1:
            maxH.append(heapq.heappop(minH))
            heapq._siftdown_max(maxH, 0, len(maxH) - 1)

        if getBalance(minH, maxH) == 0:
            result.append((maxH[0] + minH[0]) / 2)
        elif getBalance(minH, maxH) == 1:
            result.append(minH[0])
        elif getBalance(minH, maxH) == -1:
            result.append(maxH[0])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
