
# Декоратор для логирования
from datetime import datetime


def do_log(func_name, tip='start'):
    with open('log.txt', 'a') as f:
        f.write('{}: {} {}\n'.format(
            datetime.now(),  # текущее время
            tip,
            func_name  # имя запускаемой функции
        ))

def logging(func):

    def new_func(*args, **kwargs):

        do_log(func.__name__) # имя запускаемой функции

        ret = func(*args, **kwargs)

        do_log(func.__name__, 'end')

        return ret

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
