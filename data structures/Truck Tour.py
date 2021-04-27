#!/bin/python3

import os
import sys
from queue import deque


#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    n = len(petrolpumps) - 1
    q = deque(petrolpumps)
    start = 0
    passed = 0
    fuel = 0
    while passed < n:
        temp = q.popleft()
        fuel += temp[0]
        dist = temp[1]
        if fuel >= dist:
            passed += 1
            fuel -= dist
        else:
            start += passed + 1
            passed = 0
            fuel = 0
        q.append(temp)
    return start


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
