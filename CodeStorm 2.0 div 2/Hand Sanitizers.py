from collections import deque

n = int(input())
prices = list((map(int, input().split())))
money = int(input())
arr = []
for i in range(n):
    arr.append((i + 1, prices[i]))
arr.sort(key=lambda x: x[1])
count = 0
for quantity, cost in arr:
    if cost > money:
        break
    amt = cost * quantity
    if money >= amt:
        count += quantity
        money -= amt
    else:
        n = money // cost
        money -= cost * n
        count += n
print(count)
