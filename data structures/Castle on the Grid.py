#!/bin/python3

import math
import os
import random
import re
import sys
from queue import deque


# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    queue=deque()
    queue.append((startX,startY,0))
    visited=set()
    visited.add((startX,startY))
    prev_move=0
    temp_visited=set()
    while queue:
        curr=queue.popleft()
        c_x,c_y,c_move=curr[0],curr[1],curr[2]
        if c_move>prev_move:
            visited.update(temp_visited)
            temp_visited.clear()
        r,c=c_x-1,c_y
        while r>=0 and grid[r][c]!='X' and (r,c) not in visited:
            if r==goalX and c==goalY:
                return c_move+1
            if r!=c_x or c!=c_y:
                temp_visited.add((r,c))
                queue.append((r,c,c_move+1))
            r-=1
        r,c=c_x+1,c_y
        while r<len(grid) and grid[r][c]!='X' and (r,c) not in visited:
            if r==goalX and c==goalY:
                return c_move+1
            if r!=c_x or c!=c_y:
                temp_visited.add((r,c))
                queue.append((r,c,c_move+1))
            r+=1
        r,c=c_x,c_y-1
        while c>=0 and grid[r][c]!='X' and (r,c) not in visited:
            if r==goalX and c==goalY:
                return c_move+1
            if r!=c_x or c!=c_y:
                temp_visited.add((r,c))
                queue.append((r,c,c_move+1))
            c-=1
        r,c=c_x,c_y+1
        while c<len(grid) and grid[r][c]!='X' and (r,c) not in visited:
            if r==goalX and c==goalY:
                return c_move+1
            if r!=c_x or c!=c_y:
                temp_visited.add((r,c))
                queue.append((r,c,c_move+1))
            c+=1
        prev_move=c_move
    return prev_move




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
