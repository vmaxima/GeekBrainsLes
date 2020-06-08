from sys import argv
from itertools import count, cycle

name, num = argv

x = []

for i in count(int(num)):
    x.append(i)
    if i > 10:
        break
    else:
        print(i)

y = 1
for i in cycle(x):
    if y == len(x):
        break
    print(i)
    y += 1
