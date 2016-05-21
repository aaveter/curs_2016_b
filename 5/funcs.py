
# Функции


# Простая

def hello():
    print('Hello!')


# Функция с аргументами

def hello(arg1, arg2, arg3):
    pass # ничего не делает


hello(1, 2, 3)



# Функция с аргументами

def hello(arg1, arg2, arg3):
    print('Hello:', arg1, arg2, arg3)

ret = hello(10, 20, 30)
print('ret:', ret)



# Функция с выводом

def hello(arg1, arg2, arg3):
    print('Hello:', arg1, arg2, arg3)
    return arg1 + arg2 + arg3

ret = hello(1, 0, 1)
print('ret:', ret)

hello(1, 2, 3, 4) # Error
hello(1, 0) # Error



# Функция с любым кол-вом аргументов

def hello(*args):
    print('Hello:', args)

# args - получится кортежем (1, 2, 0)

hello(1, 2, 0)



# Распаковка args

def hello(*args):
    print('Hello:', *args) # операция распаковки

hello(1, 2, 0)


def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        # if b == 0:
        #     return None
        return a / b


calc(100, 200, '+')
print( calc(100, 200, '-') ) # --> -100
calc(100, 0, '/') # ---> None


calc('Hello, ', 'Max!', '+')


# Проверка на тип переменной
if type(127) is str:
    pass





