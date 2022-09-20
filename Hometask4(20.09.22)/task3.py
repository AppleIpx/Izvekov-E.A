a, b = int(input()), int(input())
remainder = b % 2
if remainder == 0:
    for i in range(b - 1, a - 1, - 2):
        print(i, end=',')
else:
    for i in range(b, a - 1, - 2):
        print(i, end=',')
