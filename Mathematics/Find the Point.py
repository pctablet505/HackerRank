#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(xp, yp, xq, yq):
    xr=2*xq-xp
    yr=2*yq-yp
    '''
    if xq-xp!=0:
        m=(yq-yp)/(xq-xp)
        yr=int(yp+m*(xr-xp))
    '''
    return (xr,yr)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
