

# Декораторы @


def func():


    def new_func():
        pass


    return new_func

ret = func()

ret() # ret являет функцией и может быть запущен





# -------------------


# Декоратор
def decorator(some_func):

    # Создаваемая функция
    def new_func():
        print('new func work!!!')
        return some_func()

    return new_func


# Функция, которую мы хотим заменить
def some_func():
    pass


# Сам процесс декорирования
some_func = decorator(some_func) # в старом стиле

# Запускаем новую функцию
some_func()


# - заменят старую ф-цию на новую, просто дополняя ее функциональностью

@decorator
def some_func_2():
    pass