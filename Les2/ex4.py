x = list(map(str, input('Введите строку:').split()))

for ind, i in enumerate(x, 1):
    print(ind, i[:10])
