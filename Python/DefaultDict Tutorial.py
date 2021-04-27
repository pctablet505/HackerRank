from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for _ in range(n):
    d['A'].append(input())
for _ in range(m):
    d['B'].append(input())
for x in d['B']:
    if d['A'].count(x) > 0:
        for i in range(len(d['A'])):
            if x == d['A'][i]:
                print(i + 1, end=' ')
        print()
    if d['A'].count(x) == 0:
        print(-1)
