# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task():
    global n                                                ## +
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_2,param_1=None):                      ## ++
    if param_1 == None:
        return None
    print( " task "+other_task.__name__+" start")           ## +
    for p in param_1:
        print("\t- count of '",p,"': ", param_2.count(p))   ## ++
    print(" task "+other_task.__name__+" stop")             ## +

smart_task()
smart_task()

other_task(('3', '4'), str(325543523))

smart_task()

# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')
procentz =0
kolichestvo =0
procents = {}
for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'иуеыаоэё' ])
    procentz += glasniye / length                                           ## +
    procent = glasniye / length
    kolichestvo+=1
    procents[name]=procent                                                  ## +

procent_total = (procentz/kolichestvo)                                      ## +
print( 'Процент гласных в словах следующий:',procent_total )

for name in procents:
    print( '\t{}: {}%'.format(name, procents[name]) )

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

# найдет в тексте html пункты меню и сделает список с их названиями