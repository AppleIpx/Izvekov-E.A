def count(n, m, k):
    if (k % n == 0 or k % m == 0) and (k < n * m):
        print('YES')
    else:
        print("NO")


count(int(input()), int(input()), int(input()))
