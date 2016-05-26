

# Исключения

x = 10 / 0

print('some other code...')


# Обработка исключений

# - чтобы программа продолжилась

try:

    open('bdfhjvbhjdf')
    x = 10 / 0

except ZeroDivisionError: # тип исключения
    print(u'Не дели на 0, друг!!')

except FileNotFoundError:
    print(u'Нет такого файла!')

except: # НЕ ИСПОЛЬЗУЙТЕ
    print(u'Неизвестная ошибка')


print('some other code...')





try:

    x = 10 / 0

except ZeroDivisionError as e: # тип исключения
    print(u'Не дели на 0, друг!!', e)


try:
    x = 10 / 0
except ZeroDivisionError as e: # тип исключения
    print(u'Не дели на 0, друг!!', e)



# Попытаться открыть файл на запись
# в НЕСУЩЕСТВУЮЩЕЙ директории и обработать
# это исключение


try:
    x = 1 #open('vghvgh/bhbhb/ghvgh/cdscd', 'w')
except FileNotFoundError as e:
    print( 'нет такого пути:', e.filename )
else:
    print('если исключения не было')
finally:
    print('это код сработает всегда')



def some_calc():
    return 10 / 2


try:
    x = some_calc()
except ZeroDivisionError:
    x = None
else:
    x *= 100
finally:
    print('x:', x)


# Генерация исключения



raise Exception('Зря включил программу...')

raise OSError()


# 1) см. ранее
# 2) калькулятор с генератором
# 3) Обработать исключение при import, если модуль не существует