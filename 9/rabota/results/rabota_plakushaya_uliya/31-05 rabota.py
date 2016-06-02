# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0
def smart_task(n):                                              ## +
    n += 1
    return n
n=smart_task(n)
print('start of smart_task # {}'.format(n) )

def other_task( param_1, param_2 ):                             ## ++
    if param_1 == None:
        return None
    print(" task ",other_task.__name__," start")                ## +
    for p in param_1:
        print("\t- count of 'p': " + str(param_2.count(p)))     ## ++
    print(" task ",other_task.__name__," stop")                 ## +
other_task(('3', '4'), str(325543523))


# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')

for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'йуеыаоэё' ])
    procent = glasniye / length
    print('Процент гласных в слове','\t{}: {}%'.format(name, procent))      ## ++- текст можно отдельно раньше написать =)


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
