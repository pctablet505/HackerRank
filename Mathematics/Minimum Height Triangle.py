#!/bin/python3

import sys
from math import ceil

def lowestTriangle(base, area):
    return ceil((area/base)*2)

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
