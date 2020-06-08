from sys import argv

name, workh, workn, extra = argv

def salary():
    global workh, workn, extra
    try:
        salary = (float(workh) * float(workn)) + float(extra)
    except ValueError:
        return 'Необходимо ввести цифровые значения'
    return salary

print('Имя скрипта: ', name)
print('Заработная плата: ', salary())
