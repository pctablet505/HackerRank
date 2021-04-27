#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def hashX(x):
    i=0
    s=set([y for y in x])
    
    binary=['0']*10
    for i in range(10):
        if str(i) in s:
            binary[i]='1'
    return int(''.join(binary),2)

def winningLotteryTicket(tickets):
    tickets=[hashX(x) for x in tickets]
    c=[0]*1024
    for x in tickets:
        c[x]+=1
    winners=0
    for i in range(1023):
        for j in range(i,1024):
            if i|j==(1<<10)-1:
                winners+=c[i]*c[j]
    winners+=c[-1]*(c[-1]-1)//2
    return winners


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
