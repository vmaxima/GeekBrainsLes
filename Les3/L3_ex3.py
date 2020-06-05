x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

def my_fun(x, y, z):
    b = sorted([x, y, z])
    return b[1] + b[2]

print(f'Сумма наибольших чисел = {my_fun(x, y, z)}')
