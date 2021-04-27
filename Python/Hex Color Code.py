import re

pattern = r'(?<!^)#[0-9a-f]{1,2}[0-9a-f]{1,2}[0-9a-f]{1,2}'
for x in range(int(input())):
    s = input()
    found = re.findall(pattern, s, re.IGNORECASE)
    for Hex in found:
        print(Hex)
