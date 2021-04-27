import re
n=int(input())
string='\n'.join((input() for _ in range(n)))
q=int(input())
for i in range(q):
    s=input()
    print(len(re.findall(r'\w{}\w'.format(s),string)))



        



