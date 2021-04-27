#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l=[]

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        #print(re.match(r'.*gmail.com$',emailID))
        if re.match(r'.*@gmail.com$',emailID):
            l.append(firstName)
    l.sort()
    for x in l:
        print(x)
