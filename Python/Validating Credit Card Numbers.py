import re
p1=r'^[456](\d){3}(-)(\d){4}(-)(\d){4}(-)(\d){4}$'
p2=r'^[456](\d){15}$'
for _ in range(int(input())):
    result='Invalid'
    s=input()
    if re.match(p1,s) or re.match(p2,s):
        s=re.sub(r'\D','',s)
        if not re.search(r'(.)\1\1\1',s):
            result='Valid'
    print(result)
