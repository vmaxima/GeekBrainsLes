mounth = int(input('Введите номер месяца: '))

x = [['Зима', 1, 2, 12], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

for i in range(len(x)):
    if mounth in x[i]:
        print(x[i][0])
