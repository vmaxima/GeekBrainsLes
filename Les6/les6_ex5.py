class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовкм'


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки - {self.title}'


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки - {self.title}'


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки - {self.title}'


pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())
