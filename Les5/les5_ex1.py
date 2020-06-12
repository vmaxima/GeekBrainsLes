x = open('file1.txt', 'w', encoding='utf-8')

stop = 0
while stop == 0:
    y = input("Введите строку: ")
    if y == '':
        stop = 1
        break
    else:
        print(y, file=x)

x.close()
