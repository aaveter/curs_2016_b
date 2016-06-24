

class Base:

    def calc_zp(self):
        return self.work_hours * self.stavka


class Worker(Base):
    stavka = 1000
    work_hours = 0

    def work_day(self):
        self.work_hours += 8


w = Worker()
w.work_day()

print( w.work_hours )
print( w.calc_zp() )