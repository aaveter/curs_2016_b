


import os


def find_python():
    # получаем имена файлов
    for filename in os.listdir('.'):
        if 'python' in filename:
            yield filename


for a in find_python():
    print( a )