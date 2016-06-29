# coding: utf-8
from threading import Thread
import time
from queue import Queue

# первый поток пишет слова
# второй их выводит

words = Queue()

# логика для потока
def append_words_in_thread(all_words):

    for w in all_words:
        words.put(w) # добавляем в очередь
        time.sleep(1)

def read_words_in_thread():

    while True:
        w = words.get() # вынимаем слово
        print(w)


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