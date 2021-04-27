from itertools import groupby

string = list(map(int, input()))
l = []
for (key, value) in groupby(string):
    l.append((len(list(value)), key))
for x in l:
    print(x, end=' ')
