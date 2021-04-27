X = []
Y = []
for _ in range(5):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

sxy = 0
sx = 0
sy = 0
sx2 = 0
sy2 = 0
for x, y in zip(X, Y):
    sxy += x * y
    sx += x
    sy += y
    sx2 += x * x
    sy2 += y * y
n = len(X)

b = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
a = (sy / n) - (b * sx / n)
# y=a+bx
y = a + b * 80
print(y)
