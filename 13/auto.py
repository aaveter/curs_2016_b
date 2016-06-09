

# Автомобили


class Auto:
    probeg = 0
    way_time = 0

    def __init__(self, marka, model, wheels, max_speed, massa):
        self.marka = marka
        self.max_speed = max_speed
        self.wheels = wheels
        self.model = model
        self.massa = massa
        #self.probeg = 0        Лучше писать в конструкторе

    def nitro_tuning(self):
        self.max_speed *= 1.1

    def move(self, way):
        self.probeg += way


class WayPart: # Участок маршрута

    def __init__(self, length, koef): # коэффициент "плохости" дороги
        self.length = length
        self.koef = koef


volvo = Auto('Volvo', 'S60', 4, 180, 2)
ural = Auto('Урал', '-', 12, 110, 20)

# volvo.move(1000)
# ural.move(300)

cars = [volvo, ural]

# Создаем маршрут, состоящий из участков дороги
way = [
    WayPart(100, 0.8),
    WayPart(50,  1.2), # Здесь была горка
    WayPart(100, 1.0), #WayPart(300, 1.0),
    WayPart(10,  0.2),
]


# for car in cars:
#     for part in way:
#         car.way_time += part.length / car.max_speed / part.koef
#         car.move(part.length)
#

class Way:

    def __init__(self, parts=[]):
        self.parts = parts

    def move(self, car):
        for part in self.parts:
            car.way_time += part.length / car.max_speed / part.koef
            car.move(part.length)


way = Way([
    WayPart(100, 0.8),
    WayPart(50, 1.2),  # Здесь была горка
    WayPart(100, 1.0),  # WayPart(300, 1.0),
    WayPart(10, 0.2),
])

way.move(volvo)
way.move(ural)


for car in cars:
    print('{}: пробег = {}, время в пути: {}'.format(
        car.marka, car.probeg, car.way_time))


