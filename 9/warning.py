


# @decorator(url='/app/')
# def func():
#     pass


# Декоратор с параметрами
# - создатель декоратора


def decorator(param):

    def real_decorator(func):

        def new_func(*args, **kwargs):
            print('work of new_func... param = {}'.format(param))
            return func(*args, **kwargs)

        return new_func

    return real_decorator


@decorator('HELLO')
def some_func():
    pass


some_func()


# 1) калькулятору добавить логирование с помощью декоратора

# 2) создаем такой декоратор, котрый дополняет функциональность
# счетчиком. То есть потом в любой момент мы сможем проверить,
# сколько раз задекорированная ф-ия была запущена.
# По окончанию программы вывести на экран информацию по запускам функций.