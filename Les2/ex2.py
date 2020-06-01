x = int(input('Введите последовательность чисел: '))

x = list(str(x))

for i in range(len(x)):
    x[i] = int(x[i])

for i in range(1, len(x), 2):
    x[i - 1], x[i] = x[i], x[i - 1]

print(*x)
