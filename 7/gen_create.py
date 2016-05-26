

# Создание универсального генератора


def gen_create():
    yield 1
    yield 2
    yield 'Hello'
    yield 3


gen = gen_create()

# for a in gen:
#     print( a )
#print( type(gen) )

x = next(gen)
print(x)

x = next(gen)
print(x)

x = next(gen)
print(x)

x = next(gen)
print(x)

x = next(gen)
print(x)


# Любой генератор заканчивается на StopIteration


def gen_create():
    for a in range(10):
        yield a

for a in gen_create():
    print( a )



def gen_create():
    while True:
        yield 'lft'

for a in gen_create():
    print( a )





from random import randint

def sites_gen():
    sites = [
        'ya.ru',
        'google.com',
        'python.org',
        'russia.ru',
    ]
    while True:
        site = sites[ randint(0, len(sites)) ]
        # либо здесь
        # if site == 'russia.ru':
        #     break
        yield site
        # либо здесь
        if site == 'russia.ru':
            break


for site in sites_gen():
    print( site )

from random import randint
while True:
    sites = [1, 2, 3]
    print( sites[randint(0, len(sites)-1)] )


# Если сгенерирруется сайт "russia.ru", то генератор завершится



# пробегаемся по файлам в текущей папке
# и выдаем имена файлов только со словом 'python'
#
# if 'python' in filename:
#     pass



