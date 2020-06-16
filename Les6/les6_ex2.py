class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, thick):
        return (self.__length * self.__width * 25 * thick) / 1000

road = Road(int(input('Введите длинну полонта (м): ')), int(input('Введите ширину полотна (м): ')))
print(f'Требуемая масса асфальта = {road.calculate(int(input("Введите толщину полотна (см): ")))} т')
