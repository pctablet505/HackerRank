#!/bin/python3

import os
import sys
def sieveOfEratosthenes():
    MAX=10000
    primes=[]
    IsPrime=[True]*MAX
    for p in range(2,MAX):
        if IsPrime[p]:
            for i in range(p**2,MAX,p):
                IsPrime[i]=False
    for p in range(2,MAX):
        if IsPrime[p]:
            primes.append(p)
    return primes
primes=sieveOfEratosthenes()
def waiter(number, q):
    global primes
    A=[[] for _ in range(q+1)]
    A[0]=number
    B=[[] for _ in range(q+1)]
    for i in range(1,q+1):
        while A[i-1]:
            x=A[i-1].pop()
            if x%primes[i-1]==0:
                B[i].append(x)
            else:
                A[i].append(x)
    res=[]
    for arr in B:
        while arr:
            res.append(arr.pop())
    while A[q]:
        res.append(A[q].pop())
    return res


        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])
    

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
