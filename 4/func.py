


# Вычисляющая функция с результатом
# def plus(arg1, arg2):
#     return arg1 + arg2
#
#
#
# print( plus(1, 10) )
#
#
# # Без результата
# def log(text):
#     open('some.log', 'a').write(text+'\n')
#
#
# ret = log("some debug")
# print( ret )
#
#
# # Заглушка
# def some_func():
#     pass
#
# some_func()
#
#
# def some_func():
#     print( 'Hello!' )
#
# print( some_func )



# python 3 !!!!!
_print = print
def print(text):
    _print('TTT: '+text)

# Универсальная функция
def some_func():
    print( 'Hello!' )

some_func()



# Анонимная функция

some_func = lambda x, y: x + y

print( some_func(10, 100) )



print( (lambda x, y: x + y)(1, 3) )


lst = [
    'Max:30',
    'Ulya:20'
]

lst.sort(key = lambda s: int(s.split(":")[1]) )

print( lst )

# Max:30   ----> ['Max, '30']  ----->  '30'  ----->  30
# ----> lambda ---->

# [30, 20]
# ---->
# [20, 30]
# ---->

# ['Ulya:20', 'Max:30']