# Наследование


# Класс 1 - родитель
# Класс 2 - наследник

class Base:
    speed = 200

    def get_way(self, t):
        return t * self.speed

class Rocket( Base ):

    amp_koef = 0.8

    def boom(self):
        print( '%'*10, 'boooom', '%'*10)

    # переопределили метод
    def get_way(self, t):
        return t * self.speed * self.amp_koef # не очень так хорошо переопределять

class Car( Base ):

    windows = ['closed', 'closed', 'closed', 'closed']

    def open_window(self, number):
        self.windows[number] = 'opened'


r = Rocket()
print( r.speed )
print( r.get_way(3) )
r.boom()

car = Car()
car.open_window(2)
print( car.windows )
print( car.get_way(3) )



# ================================


class Base:
    speed = 200

    def get_way(self, t):
        return t * self.speed

class Rocket( Base ):

    amp_koef = 0.8

    def boom(self):
        print( '%'*10, 'boooom', '%'*10)

    # переопределили метод
    def get_way(self, t):
        return Base.get_way(self, t) * self.amp_koef # не очень так хорошо переопределять


class Car( Base ):

    windows = ['closed', 'closed', 'closed', 'closed']
    wheels = [True, True, True, True]

    def open_window(self, number):
        self.windows[number] = 'opened'

    # переопределили метод
    def get_way(self, t):
        return Base.get_way(self, t) * len(self.wheels) / 4.0





