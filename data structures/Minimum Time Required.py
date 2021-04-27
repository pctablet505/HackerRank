#!/bin/python3

import math
import os
import random
import re
import sys


def minTime(machines, goal):
    machines.sort()
    min_rate = machines[0]
    max_rate = machines[-1]
    lower_bound = goal // (len(machines) / min_rate)
    upper_bound = goal // (len(machines) / max_rate)
    while lower_bound < upper_bound:
        num_days = (lower_bound + upper_bound) // 2
        tot = getNumItems(machines, goal, num_days)
        if tot >= goal:
            upper_bound = num_days
        else:
            lower_bound = num_days + 1
    return int(lower_bound)


def getNumItems(machines, goal, num_days):
    t = 0
    for x in machines:
        t += num_days // x
    return t


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
