x = input('Введите число: ')
y = input('Введите число: ')


def deli(x, y):
    try:
        x == int(x) and y == int(y)
        if int(y) == 0:
            return ('Нельзя делить на 0')
        else:
            return int(x) / int(y)
    except ValueError:
        return ('Нужно ввести число')


print(deli(x, y))
