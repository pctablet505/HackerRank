from itertools import combinations_with_replacement

string, n = input().split()
j = list(combinations_with_replacement(sorted(string), int(n)))
for i in j:
    print(''.join(sorted(i)))
