n, x = map(int, input().split())
students = [p for p in range(n)]
result = []
result.append(students)
for _ in range(x):
    result.append(list(map(float, input().split())))
result = zip(*result)
for k in result:
    print(sum(k[1::]) / x)
