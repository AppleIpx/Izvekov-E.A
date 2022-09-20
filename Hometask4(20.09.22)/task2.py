x, y = int(input()), int(input())


def positively(x, y):
    for i in range(x, y + 1, +1):
        print(i, end=",")


def negative(x, y):
    for i in range(x, y - 1, -1):
        print(i, end=",")


if x < y:
    positively(x, y)
else:
    negative(x, y)
