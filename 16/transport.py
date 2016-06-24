


class Transport:
    price = 0
    speed = 0

    def time(self, way):
        return way / self.speed

class Taxi(Transport):
    price = 45
    speed = 60

class Tram(Transport):
    price = 30
    speed = 40

class Trolleybus(Transport):
    price = 30
    speed = 50

class Autobus(Transport):
    price = 30
    speed = 40

class Metro(Transport):
    price = 35
    speed = 80

class YandexTaxi(Taxi):
    pass

class Taxovichkoff(Taxi):
    pass


way = [Tram(), Metro(), Autobus()]

t = 0
total_price = 0
for w in way:
    t += w.time(30)
    total_price += w.price

print( u'''
Вы проехали ваш маршрут за:
- {} рублей,
- {} часов.
'''.format(total_price, t) )


# ДЗ поместить рассчет маршрута в метод
# - в какой класс вы поместите?
# - какой тип метода используете?