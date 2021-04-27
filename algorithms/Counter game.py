 #!/bin/python3

import math
import os
import random
import re
import sys

def just_smaller(n):
    n=bin(n)[2:]
    return(int('1'+'0'*(len(n)-1),2))
def is_power2(n):
    n=bin(n)[2:]
    return n.count('1')==1
def Louise(n):
    if n==1:
        print('Richard')
        return
    if is_power2(n):
        x=n//2
        if n==1:
            print('Louise')
            return            
        Richard(n//2)
    else:
        x=n-just_smaller(n)
        if x==1:
            print('Louise')
            return  
        Richard(x)
def Richard(n):
    if n==1:
        print('Louise')
        return
    if is_power2(n):
        x=n//2
        if n==1:
            print('Richard')
            return            
        Louise(n//2)
    else:
        x=n-just_smaller(n)
        if x==1:
            print('Richard')
            return  
        Louise(x)

def counterGame(n):
    Louise(n)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())

        counterGame(n)
