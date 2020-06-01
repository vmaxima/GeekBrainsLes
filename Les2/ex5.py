x = [7, 5, 3, 3, 2]
quest = 'Да'
while quest == 'Да':
    quest = input('Хотите ввести число (Да/Нет):')
    if quest == 'Да':
        el = int(input('Введите число:'))
        if el < x[-1]:
            x.append(el)
        else:
            for i in range(len(x)):
                if el > x[i]:
                    x.insert(i, el)
                    break
                elif el == x[i]:
                    x.insert(len(x) - x[::-1].index(el), el)
                    break
        print(*x)
    else:
        break
