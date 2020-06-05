print('Введите параметры')


def user(name, surname, yearb, city, email, phon):
    try:
        yearb == int(yearb) and phon == int(phon)
    except ValueError:
        return ('Год рождения и телефон должны быть цифровыми значениями')
    if '@' in email:
        return (
            f"Имя: {name}, Фамилия: {surname}, Год рождения: {yearb}, Город рождения: {city}, e-mail: {email}, Телефон: {phon}")
    else:
        return ('Неверный формат эл.почты')


x = {'Имя': None, 'Фамилия': None, 'Год рождения': None, 'Город рождения': None, 'e-mail': None, 'Телефон': None}

for key in x.keys():
    x[key] = input(f'{key}: ')

print(user(name=x['Имя'], surname=x['Фамилия'], yearb=x['Год рождения'], city=x['Город рождения'], email=x['e-mail'],
           phon=x['Телефон']))
