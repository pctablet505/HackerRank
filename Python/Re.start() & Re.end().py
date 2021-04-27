import re

string = input()
sample = input()
i = 0
if re.search(sample, string[i:]):
    while i < len(string):
        match = re.search(sample, string[i:])
        if match == None:
            break
        print((match.start() + i, match.end() + i - 1))
        i += match.start() + 1
else:
    print((-1, -1))
