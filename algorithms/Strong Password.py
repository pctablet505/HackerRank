#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    c=0
    
    if not re.findall(r'[\d]',password):
        c+=1
    
    if not re.findall(r'[a-z]',password):
        c+=1
    
    if not re.findall(r'[A-Z]',password):
        c+=1
    
    if not re.findall(r'[\!@#\$%^&\*\(\)\-\+]',password):
        c+=1
    
    if n+c<6:

        c+=6-(n+c)
    
    
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
