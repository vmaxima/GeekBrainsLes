import json

x = open('text_7.txt', 'r', encoding='utf-8')
js = open('text_71.json', 'w', encoding='utf-8')

my_dict = {}
avprof = {'average_profit': 0}
totnum = 0

for i in x.readlines():
    my_dict[i.split()[0]] = int(i.split()[2]) - int(i.split()[3])
    if int(i.split()[2]) - int(i.split()[3]) > 0:
        totnum += 1

avprof['average_profit'] = sum([el for el in my_dict.values() if el > 0]) / totnum

totlist = [my_dict, avprof]

json.dump(totlist, js, ensure_ascii=False, indent=4)

x.close()
js.close()
