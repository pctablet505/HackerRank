for _ in range(int(input())):
    s=input()
    a=b=''
    for i in range(len(s)):
        if i&1:
            a+=s[i]
        else:
            b+=s[i]
    print(b,a)