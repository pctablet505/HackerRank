from math import *

c = float(input())
a = float(input())
C = atan((c / a))
p = (c / sin(C)) / 2
theta = asin(p * sin(C) / (sqrt((p ** 2) + (a ** 2) - 2 * a * p * cos(C))))
Q = round(degrees(theta))
print(str(Q) + "\xb0", end='')
