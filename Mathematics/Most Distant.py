#!/bin/python3

import os
import sys


# Complete the solve function below.
def solve(coordinates):
    leftmost = min(coordinates, key=lambda x: x[0])
    rightmost = max(coordinates, key=lambda x: x[0])
    bottom = min(coordinates, key=lambda x: x[1])
    top = max(coordinates, key=lambda x: x[1])
    points = [leftmost, rightmost, bottom, top]
    D = 0
    for x1, y1 in points:
        for x2, y2 in points:
            D = max(D, ((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return D ** 0.5


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
