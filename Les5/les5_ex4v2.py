from googletrans import Translator

x = open('text_4.txt', 'r', encoding='utf-8')
y = open('newtext_4.txt', 'w', encoding='utf-8')

translator = Translator()

for i in x.readlines():
    print(f'{(translator.translate(i.split()[0], dest="ru")).text} - {i.split()[2]}', file=y)

x.close()
y.close()
