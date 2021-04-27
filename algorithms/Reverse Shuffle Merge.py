#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    cnt=Counter(s)
    string_cnt={x:y//2 for x,y in cnt.items()}
    shuffle_cnt={x:y//2 for x,y in cnt.items()}
    stack=[]
    for ch in s[::-1]:
        if string_cnt[ch]>0:
            while stack and ch<stack[-1] and shuffle_cnt[stack[-1]]>0:
                removed=stack.pop()
                string_cnt[removed]+=1
                shuffle_cnt[removed]-=1
            stack.append(ch)
            string_cnt[ch]-=1
        else:
            shuffle_cnt[ch]-=1
    return ''.join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
