x = input('Введите слова латинскими буквами через пробел: ').split()


def int_func(x):
    y = chr(ord(x[0]) - 32)
    return y + x[1:]


for i in range(len(x)):
    print(int_func(x[i]),'', end='')
