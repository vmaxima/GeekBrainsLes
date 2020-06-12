with open('text_5.txt', 'w', encoding='utf-8') as x:
    stop = 0
    while stop == 0:
        y = input("Введите числа через пробел: ")
        if y == '':
            stop = 1
            break
        else:
            print(y, file=x)

with open('text_5.txt', 'r', encoding='utf-8') as x:
    sumtot = 0
    for i in x.readlines():
        c = i.split()
        sumtot += sum([int(i) for i in c])
    print(sumtot)
