rev = int(input('Введите выручку:'))
cost = int(input('Введите издержки:'))

rez = rev - cost
if rez > 0:
    print('Прибыль')
    print('Рентабельность выручки:', ("{:.2f}".format(rez / rev)))
    pers = int(input('Введите численность сотрудников:'))
    print('Прибыль на одного сотрудника:', ("{:.2f}".format(rez / pers)))
else:
    print('Убыток')
