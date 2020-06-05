y = 0


def sumnum():
    global y
    stop = 0
    while stop == 0:
        x = list(input('Введите числа через пробел (для отмены введите "Q"): ').split())
        for i in range(len(x)):
            if x[i].upper() == 'Q':
                stop += 1
                break
            else:
                y += int(x[i])
        if stop == 0:
            print(y)
    return y


print(sumnum())
