def dits(x, y, x1 ,y1):
    if (x + y + x1 + y1) % 2 == 0:
        print('YES')
    else:
        print('NO')
dits(int(input()), int(input()), int(input()), int(input()))