from sys import stdin, stdout 
dictionary=dict()
for i in range(int(input())):
    a,b=input().split()
    dictionary[a]=b

lines = stdin.read().splitlines()
for x in lines:
    if x in dictionary:
        print(x,'=',dictionary[x],sep='')
    else:
        print('Not found')