with open('text_3.txt', 'r', encoding='utf-8') as x:

    totsal = 0

    for i in x.readlines():
        if float(i.split()[1]) < 20000:
            print(i.split()[0])
            totsal += float(i.split()[1])
        else:
            totsal += float(i.split()[1])

    x.seek(0)
    print(f'Средняя величина дохода сотрудников: {totsal / len(x.readlines())}')
