from math import *
x, y, z = -4.5, 0.75 * 10 ** -4, -0.845 * 10 ** 2
s = ((9 + (x - y) ** 2) ** (1/3)) / (x ** 2 + y ** 2 + 2) - (exp(abs(x - y))) * tan(z) ** 3
print(round(s, 5))