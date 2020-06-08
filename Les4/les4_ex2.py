x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([i for i in x[1:] if i > x[x.index(i) - 1]])
