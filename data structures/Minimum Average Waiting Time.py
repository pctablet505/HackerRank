#!/bin/python3

import os
import sys
import heapq


#
# Complete the minimumAverage function below.
#
def minimumAverage(customers):
    n = len(customers)
    available = []
    pending = customers
    pending.sort(reverse=True)
    clock = 0
    total_waiting = 0
    while available or pending:
        if not available and pending:
            clock = max(clock, pending[-1][0])
        if pending:
            while pending and pending[-1][0] <= clock:
                heapq.heappush(available, pending.pop()[::-1])
        if available:
            current = heapq.heappop(available)
            clock += current[0]
            total_waiting += clock - current[1]
        else:
            heapq.heappush(available, heapq.heappop(pending))

    return int(total_waiting / n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
