n = int(input())
arr = list(map(int, input().split()))
_max = max(arr)
result = sum(arr) + _max
print(result)
