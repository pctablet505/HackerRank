#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
cnt = 0
for i in range(n):
    for j in range(0, n - 1):
        if a[j] >= a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            cnt += 1
print('Array is sorted in {} swaps.'.format(cnt))
print('First Element:', a[0])
print('Last Element:', a[-1])
