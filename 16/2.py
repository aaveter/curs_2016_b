

# Делегирование
# (на примере шаблона "Команда")

class Worker:

    price = 1000

    def work(self):
        return self.price


class Prorab(Worker):

    price = 5000

    def __init__(self, workers):
        self.__workers = [self] + workers

    def make_remont(self):
        summa = 0
        for w in self.__workers:
            summa += w.work()
        return summa


class Painter(Worker):

    price = 2000


class DganShut(Worker):

    def work(self):
        print(u'*^*^$'*300)
        return self.price


# Принцип "Утки"


if __name__=='__main__':


    p = Prorab(workers=[Worker(), Worker(), Painter(), DganShut()])
    total_price = p.make_remont()

    print( u'Ремонт вам обошелся в {}'.format(total_price) )