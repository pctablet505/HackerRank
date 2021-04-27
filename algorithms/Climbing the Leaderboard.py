#!/bin/python3

import math
import os
import random
import re
import sys
import bisect



def climbingLeaderboard(ranked, player):
    
    ranks=[ranked[0]]
    for x in ranked[1:]:
        if x!=ranks[-1]:
            ranks.append(x)
    ranks.reverse()
    n=len(ranks)
    
    s=0
    result=[]
    for score in player:
        s=score
        result.append(n-bisect.bisect(ranks,s)+1)
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
