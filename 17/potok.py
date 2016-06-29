# coding: utf-8
from threading import Thread
import time


# логика для потока
def run_in_other_thread(number):
    print('start of other thread #{}'.format(number))
    time.sleep(5)
    print('end of other thread #{}'.format(number))


# Создаем экземпляр потока
t = Thread(target=run_in_other_thread, args=(1,))

# Запускаем поток
t.start()

t2 = Thread(target=run_in_other_thread, args=(2,))
t2.start()


for i in range(12):
    print('ha-ha {}'.format(i))
    time.sleep(0.5)