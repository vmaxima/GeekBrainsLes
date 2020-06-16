class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police == 'Police'

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула на{direction}'

    def show_speed(self):
        return f'Скорость автомобиля - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости'
        else:
            return f'Скорость автомобиля - {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости'
        else:
            return f'Скорость автомобиля - {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        if self.is_police == True:
            return f'Полицейская машина {self.name} поехала'
        else:
            return f'Это не полицейская машина'

    def stop(self):
        if self.is_police == True:
            return f'Полицейская машина {self.name} остановилась'
        else:
            return f'Это не полицейская машина'

    def turn(self, direction):
        if self.is_police == True:
            return f'Полицейская машина {self.name} повернула на{direction}'
        else:
            return f'Это не полицейская машина'


towncar = TownCar(70, "green", "Audi", "Town")
print(f'Марка авто: {towncar.name}, цвет авто: {towncar.color}')
print(towncar.go())
print(towncar.turn('лево'))
print(towncar.show_speed())
print()
sportcar = SportCar(170, "red", "Ferrari", "Sport")
print(f'Марка авто: {sportcar.name}, цвет авто: {sportcar.color}')
print(sportcar.go())
print(sportcar.turn('лево'))
print(sportcar.show_speed())
print()
worktcar = WorkCar(30, "blu", "Kamaz", "Work")
print(f'Марка авто: {worktcar.name}, цвет авто: {worktcar.color}')
print(worktcar.go())
print(worktcar.turn('право'))
print(worktcar.show_speed())
print()
policetcar = PoliceCar(90, "wite", "Ford", "Police")
print(f'Марка авто: {policetcar.name}, цвет авто: {policetcar.color}')
print(policetcar.go())
print(policetcar.turn('право'))
print(policetcar.show_speed())
