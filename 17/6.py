# coding: utf-8
from threading import Thread, RLock     # "мьютекс"
import time

# первый поток пишет слова
# второй их выводит

words = []
mutex = RLock()

# логика для потока
def append_words_in_thread(all_words):

    for w in all_words:
        mutex.acquire() # закрываем замок

        words.append(w)

        mutex.release() # открываем замок
        time.sleep(1)

def read_words_in_thread():

    while True:
        mutex.acquire()  # закрываем замок

        if len(words) > 0:
            w = words.pop(0) # вынимаем первое слово
            print(w)

        mutex.release()  # открываем замок
        time.sleep(0.3)


all_words = [
    'hello',
    'world',
    'from',
    'python',
    '!'
]

# Создаем экземпляр потока
t = Thread(target=append_words_in_thread, args=(all_words,))

# Запускаем поток
t.start()

t2 = Thread(target=read_words_in_thread)
t2.daemon = True
t2.start()
