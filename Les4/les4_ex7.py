def fact(n):
    for i in range(1, n + 1):
        yield i


y = 1
for i in fact(int(input('Введите число: '))):
    y = y * i

print(y)
