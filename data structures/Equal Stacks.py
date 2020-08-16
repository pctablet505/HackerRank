#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    s1=h1[::-1]
    s2=h2[::-1]
    s3=h3[::-1]
    l1=sum(h1)
    l2=sum(h2)
    l3=sum(h3)

    while not(l1==l2==l3):
        if l1==max((l1,l2,l3)):
            l1-=s1.pop()
        elif l2==max((l1,l2,l3)):
            l2-=s2.pop()
        elif l3==max((l1,l2,l3)):
            l3-=s3.pop()
    return l1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
