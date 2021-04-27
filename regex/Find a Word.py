import re
string='\n'.join(input() for _ in range(int(input())))
for _ in range(int(input())):
    word=input()
    
    print(len(re.findall(r'((?<=\W)|^)%s((?=\W)|$)'%word,string)))
