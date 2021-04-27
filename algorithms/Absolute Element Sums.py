#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the playingWithNumbers function below.
def playingWithNumbers(arr, queries):
    from bisect import bisect_left, bisect_right
    positive = []
    negative = []
    for x in arr:
        if x > 0:
            positive.append(x)
        else:
            negative.append(x)
    positive.sort()
    negative.sort()
    p_sum = [positive[0]]
    for i in range(1, len(positive)):
        p_sum.append(p_sum[-1] + positive[i])
    n_sum = [negative[0]]
    for i in range(1, len(negative)):
        n_sum.append(n_sum[-1] + negative[i])
    d = 0
    result = []
    for q in queries:
        d += q
        ans = 0
        if d > 0 and d < 2000:
            ans += p_sum[-1] + d * len(positive)
            nind = bisect_left(negative, -d)
            if nind == 0:
                ans += d * len(negative) + n_sum[-1]
            elif nind == len(negative):
                ans += -n_sum[-1] - d * len(negative)
            elif 0 < nind < len(negative):
                ans += -n_sum[nind - 1] - d * nind
                ans += d * (len(negative) - nind) + n_sum[-1] - n_sum[nind - 1]
        elif d >= 2000:
            ans += p_sum[-1] + d * len(positive)
            ans += d * len(negative) + n_sum[-1]
        elif d == 0:
            ans += p_sum[-1] - n_sum[-1]
        elif d < 0 and d > -2000:
            ans += -n_sum[-1] - d * len(negative)
            pind = bisect_right(positive, -d)
            if 0 < pind < len(positive):
                ans += -d * pind - p_sum[pind - 1]
                ans += p_sum[-1] - p_sum[pind - 1] + d * (len(positive) - pind)
            elif pind == len(positive):
                ans += p_sum[-1] - d * (len(positive))
            elif pind == 0:
                ans += p_sum[-1] + d * (len(positive))
        elif d <= -2000:
            ans += -d * (len(negative)) - n_sum[-1]
            ans += -d * len(positive) - p_sum[-1]
        result.append(ans)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
