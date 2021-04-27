
n,p=map(int,input().split())
string=input()

def coeff(string):
    
    arr=[]
    last=''
    for c in string:
        if c==last:
            arr[-1]+=1
        else:
            arr.append(1)
        last=c
    if len(arr)<3:
        return [[],0]
    return arr[1:len(arr)-1]

def minimise(arr,p):
    if p==0:
        return sum(arr)
    n=len(arr)
    if n<2*p:
        return 0 
    s=sum(arr[2*p:])
    variations=[s]
    for i in range(2*p):
        ns=variations[-1]+arr[2*p-1-i]-arr[-i-1]
        variations.append(ns)      

    return min(variations)
        


arr=coeff(string)
print(minimise(arr,p))