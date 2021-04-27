from decimal import Decimal
from math import sqrt, floor,ceil
primes_set=set([2])
def isPrime(n):
    if n<=1:
        return False
    if n in primes_set:
        return True    
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    else:
        primes_set.add(n)
        return True

if __name__=='__main__':
    n=int(input())
    for i in range(n):
        x=Decimal(int(input()))
        if isPrime(x):
            print('Prime')
        else:
            print('Not prime')