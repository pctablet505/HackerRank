from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(sum(arr)/n)
mid= n//2
if n&1==0:
    print(((arr[mid-1]+arr[mid])/2))
else:
    print(arr[mid])
print(Counter(arr).most_common(1)[0][0])
