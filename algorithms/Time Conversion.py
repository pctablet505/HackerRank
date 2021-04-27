#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    string=''
    hr,mn,se=map(int,s[:-2].split(':'))
    t=s[-2:]
    if t=='AM' or t=='am':
        hr%=12
    if t=='pm' or t=='PM' and hr<12:
        hr=(hr+12)%24
    return('{:02d}:{:02d}:{:02d}'.format(hr,mn,se))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
