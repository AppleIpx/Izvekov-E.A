n = int(input())
a = 1
y = 0
sum = 0
for i in range(1, n + 1):
    b = a
    a = b + y
    y = b
    sum += b
print(sum)
