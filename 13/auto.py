

# Автомобили


class Auto:

    wheels = 4
    max_speed = 60
    massa = 0

    def __init__(self, marka, model, wheels, max_speed, massa):
        self.marka = marka
        self.max_speed = max_speed
        self.wheels = wheels
        self.model = model
        self.massa = massa

    def nitro_tuning(self):
        self.max_speed *= 1.1


volvo = Auto('Volvo', 'S60', 4, 180, 2)
ural = Auto('Урал', '-', 12, 110, 20)