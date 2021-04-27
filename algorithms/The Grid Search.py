#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    m = len(G)
    n = len(G[0])
    r = len(P)
    c = len(P[0])

    for i in range(m):
        for j in range(n):
            if G[i][j] == P[0][0]:

                if i + r <= m and j + c <= n:
                    f = True
                    for x in range(r):
                        # print(P[x],G[i+x][j:j+len(P[x])])
                        if P[x] == G[i + x][j:j + len(P[x])]:
                            continue
                        f = False
                        break
                    if f:
                        return 'YES'
                    '''
                    f=True
                    for x in range(len(P)):
                        for y in range(len(P[0])):
                            if P[x][y]==G[x+j][y+i]:
                                continue
                            else:
                                f=False
                                break
                    if f:
                        return 'YES'
                    '''
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
