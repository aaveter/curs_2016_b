
# Именованные аргументы

def vivod(name, old, mark):
    print('Имя:', name, 'Возраст:', old, 'Оценка:', mark)

def students_vivod(students):
    for student in students:
        vivod(
            name = student[0],
            old = student[1],
            mark = student[2])


def students_vivod(students):
    for student in students:
        vivod(
            old = student[1],
            name = student[0],
            mark = student[2])



# Значение по-умолчанию

def vivod(name, old, mark, separator=' '):
    lst = [name, old, mark]
    print(separator.join(lst))

#vivod(name='Ilya', old='27', mark='5')
vivod(name='Ilya', old='27', mark='5', separator='\n')


# Именованные аргументы дб справа

vivod('Ilya', '27', '5', '\n')
vivod('Ilya', '27', '5', separator='\n')
vivod('Ilya', '27', mark='5', separator='\n')
vivod('Ilya', '27', separator='\n', mark='5')

#vivod(name='Ilya', old='27', mark='5', '\n') # ERROR



def func(a=1, b=2, c=3):
    pass

func(c=20, a=30)



def calc(a, b, operation="+", *args):
    summa = sum(args)


    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        # if b == 0:
        #     return None
        return a / b



def calc(a, b, operation=None):
    if operation == '+' or operation == None:
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        # if b == 0:
        #     return None
        return a / b


print( calc(10, 20) )