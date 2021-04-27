import re

for i in range(int(input())):
    s = input()
    result = False
    if len(s) == 10:
        if len(re.findall('[a-zA-Z0-9]', s)) == 10:
            if len(re.findall('[A-Z]', s)) >= 2:
                if len(re.findall('\d', s)) >= 3:
                    if not re.search(r'(.).*\1', s):
                        result = True
    if result:
        print("Valid")
    else:
        print("Invalid")
