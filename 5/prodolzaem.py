

# Функция внутри функции

def func():

    x = 100

    def other_func():
        print('hello!')

    other_func()



func()


# Полезный вариант


def func(count):

    def other_func(n): # принимает на вход n
        print('hello!', n)

    for i in range(count):
        other_func(i)

func(1000)


# global и nonlocal

GLOB = 123

def func():
    global GLOB
    GLOB = 170

func()
print(GLOB)



GLOB = 'GLOB'

def func():

    NE_GLOB = 'NE GLOB'

    def other_func():
        global GLOB

        GLOB = 'GLOB after other_func!!!'

        NE_GLOB = 'NE GLOB 1'

        print('NE_GLOB:', NE_GLOB)

        print('GLOB in other_func:', GLOB)

    other_func()

    print('old NE_GLOB:', NE_GLOB)
    print('GLOB in func:', GLOB)


func()



# nonlocal

def func():

    NE_GLOB = 'NE GLOB'

    def other_func():
        nonlocal NE_GLOB # ТОЛЬКО python 3!!!!
        NE_GLOB = 'NE GLOB after other_func'

    other_func()

    print('NE_GLOB:', NE_GLOB)

func()




def creater():

    def shower(a, b):
        print('a: {} b: {}'.format(a, b))

    def summer(a, b):
        return a + b

    def empty():
        pass

    return shower, summer


new_shower, summer = creater()


new_shower(100, 102)



# ЗАМЫКАНИЯ


def creater(a, b):

    def shower():
        print('a: {} b: {}'.format(a, b))

    return shower


new_shower = creater('hello', 'by')

new_shower()
new_shower()
new_shower()






def counter(n):

    count = 0
    def gen():
        nonlocal count
        count += 1
        for i in range(n):
            print(count, '-->', i)

    return gen


#counter(n=10)()   # так можно сразу запустить

gen = counter(n=3)

gen()
gen()
gen()





def webserver(url):

    def ya_ru():
        return '<html>Yandex</html>'

    def google():
        return '<html>Google</html>'

    urls = {
        'ya.ru': ya_ru,
        'google.com': google,
    }


    return urls[url]()


print( webserver(url='ya.ru', name='Alex') )


# 1. приветсвие от Yandex-а b от Гугла

# 2. сделать программу калькулятор
# вечный цикл
# вычисление того, что получили через input
# EXIT - выход из программы

# 3. сделать функцию: на входе кол-во = длина списка
# на выходе список случайных чисел
# модуль random