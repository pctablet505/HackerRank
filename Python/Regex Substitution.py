import re

for _ in range(int(input())):
    s = input()
    s = re.sub('(?<= )(&&)(?= )', 'and', s)
    s = re.sub('(?<= )(\|\|)(?= )', 'or', s)
    print(s)
