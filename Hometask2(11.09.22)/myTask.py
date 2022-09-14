from math import *
x, y, z = 16.55 * 10 ** -3, -2.75, 0.15
s = sqrt(10 * (x ** (1/3) + x ** (y + 2))) * (asin(z) ** 2 - abs(x - y))
print(s)