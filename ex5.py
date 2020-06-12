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

# Вариант с форматированием f-строк

rev = int(input('Введите выручку:'))
cost = int(input('Введите издержки:'))

rez = rev - cost
if rez > 0:
    print('Прибыль')
    print(f"Рентабельность выручки: {rez / rev:.2f}")
    pers = int(input('Введите численность сотрудников:'))
    print(f"Прибыль на одного сотрудника: {rez / pers:.2f}")
else:
    print('Убыток')
