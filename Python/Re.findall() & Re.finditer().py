import re

string = input()
v = 'aeiouAEIOU'
c = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
pattern = r"(?<=[%s])([%s]{2,})(?=[%s])" % (c, v, c)
result = re.findall(pattern, string)
# print(result)
if result == []:
    print(-1)
for y in result:
    print(y)
