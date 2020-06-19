class Ceil:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num >= 0:
            return self.num - other.num
        else:
            return f'разность количества ячеек меньше 0'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num

    def make_order(self, num_cel):
        self.num_cel = num_cel
        for i in range(self.num // self.num_cel):
            print('*' * self.num_cel)
        if self.num % self.num_cel > 0:
            print('*' * (self.num % self.num_cel))
        return ''

    def __str__(self):
        return f'{self.num}'


ceil_1 = Ceil(15)
ceil_2 = Ceil(12)
print(ceil_1)
print(ceil_2)
print(ceil_1 + ceil_2)
print(ceil_1 - ceil_2)
print(ceil_1 * ceil_2)
print(ceil_1 / ceil_2)
print(ceil_1.make_order(5))
