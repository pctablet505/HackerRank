from itertools import combinations as cb
n=int(input())
s=input().split()
r=int(input())
l=list(cb(s,r))
c=0
for x in l:
    if 'a' in x:
        c+=1
print('{:.3f}'.format(c/len(l)))
