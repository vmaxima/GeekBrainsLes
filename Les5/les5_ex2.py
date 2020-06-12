with open('file1.txt', 'r', encoding='utf-8') as x:

    for i in enumerate(x.readlines(), 1):
        print(i[0], i[1].count(' ') + 1)
