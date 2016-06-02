# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task():                                           ## +
    global n                                                ## +
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_1, param_2 ):                         ## ++
    print( " task ", other_task.__name__, " start")         ## +
    for p in param_1:
        print("\t- count of '"+p+"':", param_2.count(p))    ## ++
    print(" task "+other_task.__name__+" stop")             ## +

smart_task()
smart_task()

other_task(('3', '4'), str(325543523))   #'325543523'       ## +

smart_task()


# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')
procents = {}                                               ## +

for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'уеыаоэёяию' ]) ## +
    procent = 100 * glasniye / length                       ## +
    # можно рассчет согласных                               ## +
    procents[name] = procent                                ## +


print( 'Процент гласных в словах следующий:' )

for name in procents:
    print( '\t{:20}: {:.2f}%'.format(name, procents[name]) )


# 3. Написать функцию, которая...

html = '''
<html>
    <body>
        <p>Some text..</p>
        <ul id='some_list'>
            <li>Ненужный элемент</li>
        </ul>
        <p>Some text..</p>
        <ul id='menu'>
            <li>Изделия</li>
            <li>Функциональность</li>
            <li>История</li>
            <li>Конфигуратор</li>
        </ul>
    </body>
</html>
'''

# найдет в тексте html пункты меню и
# сделает список с их названиями

def get_menu(text):                     ## +

    start_s = "<ul id='menu'>"
    start_s_len = len(start_s)
    start = text.find(start_s)
    if start < 0:
        return []
    end = text.find('</ul>', start + start_s_len)

    menu = text[ start + start_s_len : end ]
    menu = menu.strip().replace('\n', '').replace('\r', '')
    menu = menu.replace('\t', '')
    menu = menu.replace(' ', '')
    #print('|'+menu+'|')

    lst = menu.split('</li>')
    result = []
    for a in lst:
        a = a.strip('<li>')
        if len(a) > 0:
            #print('a:', a)
            result.append(a)

    return result




menu = get_menu(html)

print('menu:', menu)



