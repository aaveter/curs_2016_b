

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