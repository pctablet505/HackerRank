n=int(input())
numbers=list(map(int,input().split()))
print(all(map(lambda x:x>=0,numbers)) and (any(map(lambda x:str(x)==str(x)[::-1],numbers))))
