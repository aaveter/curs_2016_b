
# Декоратор для логирования
from datetime import datetime

def logging(func):

    def new_func(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write('{}: {}\n'.format(
                datetime.now(),        # текущее время
                func.__name__          # имя запускаемой функции
            ))
        return func(*args, **kwargs)

    return new_func


@logging
def calc(a, b):
    return a + b

@logging
def three():
    print('three')


if __name__=='__main__':
    print( calc(7, 3) )
    three()
