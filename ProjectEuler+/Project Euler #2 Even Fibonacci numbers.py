#!/bin/python3

import sys
fib=[0,1,1]
for i in range(10**5):
    fib.append(fib[-1]+fib[-2])
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    res=2
    f1=0
    f2=2
    while f2<n:
    
        f3=4*f2+f1
        
        if f3%2==0 and f3<n:
            res+=f3
        f1=f2
        f2=f3
    print(res)
    

