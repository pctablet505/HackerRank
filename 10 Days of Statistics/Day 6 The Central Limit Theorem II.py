import math

n = 100
mean = 2.4
stddeviation = 2

m1 = n * mean
std1 = stddeviation * (n ** 0.5)
x = 250
qx = (1 / 2) * (1 + math.erf((x - m1) / (std1 * (2 ** 0.5))))
print(qx)
