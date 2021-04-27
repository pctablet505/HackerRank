a=bin(int(input()))[2:]

M=0
n=0
for i in range(len(a)):
    if a[i]=='1':
        n+=1
    else:
        M=max(M,n)
        n=0
M=max(M,n)     
print(M)
