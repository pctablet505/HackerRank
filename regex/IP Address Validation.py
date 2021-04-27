import re
IPv4=r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
IPv6=r'^[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}$'
for i in range(int(input())):
    s=input()
    if re.match(IPv4,s):
        arr=map(int,s.split('.'))
        t=True
        for x in arr:
            if x<256:
                continue
            t=False
        if t:
            print('IPv4')
        else:
            print('Neither')
    elif re.match(IPv6,s):
        print('IPv6')
    else:
        print('Neither')

