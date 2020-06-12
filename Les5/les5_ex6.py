import re
with open('text_6.txt', 'r', encoding='utf-8') as x:
    my_list = {}
    for i in x.readlines():
        my_list[i.split(':')[0]] = sum([int(el) for el in re.findall(r'\d+', i)])

    print(my_list)
