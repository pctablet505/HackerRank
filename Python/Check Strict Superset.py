A = set(map(int, input().split()))
n = int(input())
flag = True
for _ in range(n):
    B = set(map(int, input().split()))
    flag = A.issuperset(B)
    if not flag:
        break
print(flag)
