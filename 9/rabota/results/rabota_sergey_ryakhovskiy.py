# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task():
    global n                                                        ## +
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_2, param_1=None ):                            ## ++
    if param_1 == None:
        return None
    print( " task ", other_task.__name__, " start")                 ## +
    for p in param_1:
        print("\t- count of '", p, "': " + str(param_2.count(p)))   ## ++
    print(" task ", other_task.__name__, " stop")                   ## +

smart_task()
smart_task()

other_task(str(325543523), ('3', '4'))

smart_task()


# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')
procents={}                                                                 ## +

for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'аеёиоуыэюя' ])  ## +
    procent = glasniye / length
    procents[name] = procent                                                ## +

print( 'Процент гласных в словах следующий:' )

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

def search(html):
    isMenu = False
    listMenu = []
    with open('html.txt','w') as f:
        f.write(html)

    with open('html.txt','r') as f:
        for row in f:
            if len(row) > 0:
                if not isMenu and row.find("menu")>0:
                    isMenu = True
                else:
                    if isMenu and row.find("<li>")>0:
                        listMenu.append(row.replace(' ','').replace('<li>','').replace('</li>\n',''))
                    else:
                        isMenu = False

    return listMenu

print(search(html))

# впринципе рабочий вариант
                                                                ## +++

# найдет в тексте html пункты меню и сделает список с их названиями