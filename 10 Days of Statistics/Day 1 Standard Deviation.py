n = int(input())
arr = list(map(int, input().split()))
arr.sort()
u = sum(arr) / n
std_deviation = (sum(map(lambda x: (x - u) ** 2, arr)) / n) ** 0.5
print(std_deviation)
