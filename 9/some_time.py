

from datetime import datetime


def now_showing(func):

    def new_func():
        print(datetime.now())
        func()

    return new_func


@now_showing
def one():
    print('one')

@now_showing
def two():
    print('two')

@now_showing
def three():
    print('three')


one()
two()
three()




#=====================================
from datetime import datetime

def now_showing(func):

    def new_func(a, b):
        print(datetime.now())
        return func(a, b)

    return new_func


@now_showing
def calc(a, b):
    return a + b

print( calc(7, 3) )


#=====================================
from datetime import datetime

def now_showing(func):

    def new_func( *args, **kwargs ): # принимаем любое кол-во аргументов
        print(datetime.now())
        return func( *args, **kwargs ) # распаковка

    return new_func


@now_showing
def calc(a, b):
    return a + b

@now_showing
def three():
    print('three')

print( calc(7, 3) )
three()
