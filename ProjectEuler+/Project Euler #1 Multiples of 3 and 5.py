#!/bin/python3

import sys
from decimal import Decimal



t = int(input().strip())
def sumAP(a,n,d):
    n=n+1
    return (n/2)*(2*a+(n-1)*d)
for a0 in range(t):
    n = Decimal(input().strip())
    result=0
    result+=sumAP(0,((n-1)//3),3)
    result+=sumAP(0,(n-1)//5,5)
    result-=sumAP(0,(n-1)//15,15)
    print(int(result))
