
import os

# Проверка существования файла
# Чтение из файла

if os.path.exists('1.py'):

    f = open('1.py', encoding='utf-8') # открытие файла

    #data = f.read() # чтение целиком всего файла

    data_100 = f.read(3)
    print( f.tell() ) # позиция в файле

    data_100_2 = f.read(3)
    print( f.tell() )

    f.seek(0) # перейти в конкретную позицию
    print( f.tell() )


    f.close() # закрыть файл