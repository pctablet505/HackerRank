#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict,Counter

# Complete the sherlockAndAnagrams function below.
from collections import Counter,defaultdict
def getHash(s):
    res=[0]*26
    c=Counter(s)
    for x in c:
        res[(ord(x)-97)]=c[x]
    return res
def add(h1,h2):
    res=[0]*26
    for i in range(26):
        res[i]=h1[i]+h2[i]
    return res
def sub(h1,h2):
    res=[0]*26
    for i in range(26):
        res[i]=h1[i]-h2[i]
    return res
        
def plus(h1,c):
    h1=list(h1)
    h1[ord(c)-97]+=1
    return tuple(h1)
def to_str(h):
    
    s=''
    for i in range(26):
        s+=(chr(97+i))*h[i]
    return s
def sherlockAndAnagrams(s):
    d=dict()
    d[0]=getHash(s[0])
    for i in range(1,len(s)):
        d[i]=plus(d[i-1],s[i])
    
    hashes=defaultdict(int)
    for i in range(len(s)):
        for j in range(i,len(s)):
            if i>0:                
                x=tuple(sub(d[j],d[i-1]))           
            else:                
                x=tuple(d[j])
            hashes[x]+=1
            
    #print(hashes)
    res=0
    for h in hashes:        
        n=hashes[h]
        
        if n>1:
            res+=(n*(n-1))//2
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
