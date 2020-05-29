n = int(input('Введите число:'))

max = 0
x = 10

while x > 9:
    x = n // 10
    b = n % 10
    a = x % 10
    if max < b:
        max = b
    if max < a:
        max = a
    n = x

print(max)
