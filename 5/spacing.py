


# глобальная
GLOB = 'SOME GLOBAL'


def func():
    global GLOB # возможность редактирования глобальной переменной
    print(GLOB)

    x = 'some local'
    print(x)

    x = 'new local'
    print(x)

    GLOB = 'NEW GLOB'


x = 'global x'

func()

x = 'global x @@'


def new_func():
    print('x in new_func:', x)


new_func()