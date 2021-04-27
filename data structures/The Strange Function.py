#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumValue function below.
def maximumValue(a):
    stack=[]
    answer=float('-inf')
    for x in a:
        for i in range(len(stack)):
            stack[i][0]=math.gcd(stack[i][0],x)
            stack[i][1]+=x
            if x>stack[i][2]:
                stack[i][1]-=x-stack[i][2]
                stack[i][2]=x
        stack.append([x,0,x])
        newStack=[]
        for i in range(len(stack)):
            if newStack and newStack[-1][0]==stack[i][0]:
                if newStack[-1][1]<=stack[i][1]:
                    if newStack[-1][1]+newStack[-1][2]>stack[i][1]+stack[i][2]:
                        newStack.append(stack[i])
                        continue
                    newStack[-1][1]=stack[i][1]
                    newStack[-1][2]=stack[i][2]
            else:
                newStack.append(stack[i])
        stack=newStack[:]
        answer= max(answer,max(abs(stack[i][0])*stack[i][1] for i in range(len(stack))))
    return answer



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = maximumValue(a)

    fptr.write(str(result) + '\n')

    fptr.close()
