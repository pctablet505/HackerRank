k = int(input())
arr = list(map(int, input().split()))
roomno = set(arr)
print(((sum(roomno) * k) - sum(arr)) // (k - 1))
