import re
for _ in range(int(input())):
    r=True
    try:
        re.compile(input())
    except:
        r=False
    print(r)
