# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:45:45 2020

@author: rahul
"""
'''This code is working in pypy3'''
'''the complexity of this algorithm is n*log(max(arr)) and 
I have tried red black trees with same time complexity n*log(n)
all gave TLE in python3.
The editorial solution is mergeSort method but that too has same complexity.

'''


def update(tree, max_ind, index, val):
    while index <= max_ind:
        tree[index] += val
        index += index & (-index)


def getSum(tree, index):
    sum_ = 0
    while index > 0:
        sum_ += tree[index]
        index -= index & (-index)
    return sum_


def getInvCount(arr, n):
    res = 0
    Max = max(arr)
    BIT = tree = [0] * (Max + 1)
    for i in range(n - 1, -1, -1):
        res += getSum(tree, arr[i] - 1)
        update(tree, Max, arr[i], 1)
    return res


def insertionSort(arr):
    return getInvCount(arr, len(arr))


t = int(input())
s = ''

for t_itr in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = insertionSort(arr)
    s += str(result) + '\n'
print(s)
