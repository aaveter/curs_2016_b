


# Бутерброд


def bread(func):

    def new_func():
        func()
        print('/////////')

    return new_func


def cheese(func):

    def new_func():
        func()
        print('~~~~~~~~~')

    return new_func


def tomato(func):

    def new_func():
        func()
        print('@@@@@@@@@')

    return new_func


@bread  # 5
@cheese # 4
@tomato # 3
@cheese # 2
@bread  # 1
def sandwitch():
    pass


sandwitch()



from datetime import datetime
datetime.now() # текущее время

