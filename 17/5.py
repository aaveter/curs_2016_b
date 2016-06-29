# coding: utf-8
from threading import Thread, RLock     # "мьютекс"
import time

threads = []
mutex = RLock()

# логика для потока
def run_in_other_thread(number):

    mutex.acquire() # закрываем замок
    if not number in threads:
        threads.append(number) # Могло случайно быть добавлено 2 одинаковых номера
    mutex.release() # открываем замок

    print('start of other thread #{}'.format(number))
    time.sleep(3)
    print('end of other thread #{}'.format(number))

    mutex.acquire()
    if number in threads:      # Опасность !!!
        threads.remove(number) # ошибка, если кто-то успел удалить number
    mutex.release()


# Создаем экземпляр потока
t = Thread(target=run_in_other_thread, args=(1,))

# Запускаем поток
t.start()

t2 = Thread(target=run_in_other_thread, args=(1,))
t2.start()

for i in range(10):
    print('ha-ha {}: {}'.format(i, threads))
    time.sleep(0.5)

# Хочу завершения сразу