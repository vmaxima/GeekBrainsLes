from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, hight):
        self.size = size
        self.hight = hight

    @property
    def get_tot_expen(self):
        return f'Общая площадь ткани - {((self.size / 6.5) + 0.5) + ((self.hight * 2) + 0.3):.4}'


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def expen(self):
        return f'Площадь ткани для пальто - {((self.size / 6.5) + 0.5):.3}'


class Suit(Clothes):

    def __init__(self, hight):
        self.hight = hight

    def expen(self):
        return f'Площадь ткани для костюма - {((self.hight * 2) + 0.3):.3}'


coat_1 = Coat(46)
clothes = Clothes(48, 1.76)
print(coat_1.expen())
suit_1 = Suit(1.78)
print(suit_1.expen())
print(clothes.get_tot_expen)
