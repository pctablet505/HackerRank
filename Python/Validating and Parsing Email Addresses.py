import email.utils
import re

for _ in range(int(input())):
    name, add = email.utils.parseaddr(input())
    pattern = r'[a-zA-Z](\w|\.|-|_)*@[a-zA-Z]*\.[a-zA-Z]{1,3}$'
    found = re.match(pattern, add)
    # print(found)
    if found:
        print(email.utils.formataddr((name, add)))
