#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    c1=Counter(s1)
    c2=Counter(s2)
    letters=set(c1.keys()).union(set(c2.keys()))
    diff=0
    for x in letters:
        if x in c1:
            if x in c2:
                diff+=abs(c1[x]-c2[x])
            else:
                diff+=c1[x]
        else:
            diff+=c2[x]
    return diff



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
