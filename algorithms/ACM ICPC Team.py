#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    
    n=len(topic)
    ls=len(topic[0])
    res=[0]*(ls+1)
    for i in range(n):
        for j in range(i+1,n):
            c=0
            for k in range(ls):
                if topic[i][k]=='1' or topic[j][k]=='1':
                    c+=1
            res[c]+=1
    for i in range(ls,-1,-1):
        if res[i]>0:
            return [i,res[i]]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
