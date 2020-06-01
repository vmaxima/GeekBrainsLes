prod = []
analis = {"Название": [],"Цена": [],"количество": [],"ед": []}

x = 1
quest = 'Да'
while quest == 'Да':
    quest = input('Хотите добавить товар (Да/Нет):')
    if quest == 'Да':
        mdic = {"Название": None,"Цена": None,"количество": None,"ед": None}
        mdic["Название"] = input("Введите название товара: ")
        mdic["Цена"] = int(input("Введите цену товара: "))
        mdic["количество"] = int(input("Введите количество товара: "))
        mdic["ед"] = input("Введите единицы измерения: ")
        prod.append((x, mdic))
        x += 1
    else:
        for i in range(len(prod)):
            analis["Название"].append(prod[i][1]["Название"])
            analis["Цена"].append(prod[i][1]["Цена"])
            analis["количество"].append(prod[i][1]["количество"])
            analis["ед"].append(prod[i][1]["ед"])

print()
for key, value in analis.items():
    print(f"{key}: {value}")
