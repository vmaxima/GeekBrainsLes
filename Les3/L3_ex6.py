x = input('Введите слово: ').split()


def int_func(x):
    return x.capitalize()


for i in range(len(x)):
    print(int_func(x[i]),'', end='')

