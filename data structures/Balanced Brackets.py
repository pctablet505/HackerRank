#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    table = {')': '(', '}': '{', ']': '['}
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        elif x not in table:
            stack.append(x)
        elif table[x] == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(x)
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
