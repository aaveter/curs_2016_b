
# Множественное наследование


class A:
    name = 'Не задано'

class B:
    age = 0

class C(A, B):
    pass


c = C()
print( c.name, c.age )


# ----------------------

class A:
    name = 'Не задано'

class B:
    name = 'Нету'
    age = 0

class C(A, B):
    pass

c = C()
print( c.name, c.age )

print(
    C.__base__,
    C.__bases__
)



# -------------------------


class Worker:

    work_hours = 0

    def work_day(self):
        self.work_hours += 8


class LgotWorker(Worker):

    def work_day(self):
        self.work_hours += 4


class MaxLgotWorker(Worker): # ТАК НЕЛЬЗЯ

    def work_day(self):
        self.work_hours += 2


m = MaxLgotWorker()
m.work_day()

print( m.work_hours )







