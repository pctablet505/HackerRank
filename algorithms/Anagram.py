#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
def anagram(s):
    l=len(s)
    if l&1:
        return -1
    c1=Counter([x for x in s[:l//2]])
    c2=Counter([x for x in s[l//2:]])
    print(c1,c2)
    m1=0
    for x in c1:
        if x in c2:
            if c1[x]-c2[x]>0:
                m1+=c1[x]-c2[x]
        else:
            m1+=c1[x]
    return m1
    
    '''
    m2=0
    for x in c2:
        if x in c1:
            m2+=abs(c1[x]-c2[x])
        else:
            m2+=c2[x]
    
    return min(m1,m2)
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
