#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    M=0
    m=0
    for i in range(1,n+1):
        if n%i==0:
            s=sum([int(x) for x in str(i)])
            if s>M:
                M=s
                m=i
            elif s==m:
                if i<m:
                    m=i
    print(m)





