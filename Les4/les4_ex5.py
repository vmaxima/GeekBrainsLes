from functools import reduce


def my_func(x, y):
    return x + y


print(reduce(my_func, ([i for i in range(100, 1002, 2)])))
