class Worker:
    def __init__(self, name, surname, position, incom):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = incom[self.position]


class Position(Worker):
    def __init__(self, name, surname, position, incom):
        super().__init__(name, surname, position, incom)

    def get_full_name(self):
        return f'{self.name}, {self.surname}'

    def get_total_incom(self):
        return f'{self._incom["wage"] + self._incom["bonus"]}'


inc = {'Директор': {'wage': 200000, 'bonus': 10000}, 'Уборщик': {'wage': 10000, 'bonus': 1000}}


position = Position('Вася', 'Пупкин', 'Уборщик', inc)
print(position.get_full_name())
print(position.get_total_incom())
