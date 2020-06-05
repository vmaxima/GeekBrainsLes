x = float(input('Ведите число: '))
y = int(input('Введите отрицательную степень числа: '))

def sq(x, y):
    if y >= 0:
        return ('Число возведения в степень должно быть отрицательным')
    else:
        return float(x) ** y


def sq2(x, y):
    if y >= 0:
        return ('Число возведения в степень должно быть отрицательным')
    else:
        num = 1 / x
        for i in range(1, abs(y)):
            num = num / x
        return num


print(sq(x, y))
print(sq2(x, y))
