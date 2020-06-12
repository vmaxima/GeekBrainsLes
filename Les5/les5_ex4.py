x = open('text_4.txt', 'r', encoding='utf-8')
y = open('newtext_4.txt', 'w', encoding='utf-8')

voc = {'1': ['One', 'Один'], '2': ['Two', 'Два'], '3': ['Three', 'Три'], '4': ['Four', 'Четыре']}

for i in x.readlines():
    if i.split()[2] in voc.keys():
        print(f'{voc.get(i.split()[2])[1]} - {i.split()[2]}', file=y)

x.close()
y.close()
