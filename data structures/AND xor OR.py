import os
import sys
from queue import LifoQueue

class Stack:
    def __init__(self):
        self.items=[]
        self.size=0
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        self.size-=1
        return self.items.pop()
    def isEmpty(self):
        return self.size==0
    def peek(self):
        return self.items[-1]
def andXorOr(a):
    stack=Stack()
    mx=a[0]^a[1]
    for i in a:
        popped=True
        while not stack.isEmpty():
            top=stack.peek()
            Si=i^top
            if Si>mx:
                mx=Si
            if i<top:
                stack.pop()
            else:
                break
        stack.push(i)
    return mx
            

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
