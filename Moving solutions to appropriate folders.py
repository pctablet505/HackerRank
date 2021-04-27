# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:10:33 2021

@author: rahul
"""
import os


algorithm = []
ds = []
ai = []
python = []
c=[]
regex=[]
cpp=[]
maths=[]
java=[]
_30days=[]
_10=[]



banned = ['\\', '/', '!', '*', '"', '<', '>', '?', ':']

f = open('Solve Algorithms HackerRank.txt')
li = f.readlines()
f.close()

for i in range(len(li)):
    if 'Success Rate' in li[i].strip():
        s=li[i-1].strip()
        for x in banned:
            s = s.replace(x, '')
        algorithm.append(s)





# for x in os.listdir('hackerrank\\Master'):
#     if x.split('.')[0] in cpp:
#         print(x)
#         #os.makedirs('hackerrank\\10 Days of Statistics\\')
#         os.rename('hackerrank\\Master\\'+x, 'hackerrank\\C++\\'+x)

    