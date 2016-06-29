
# import os
#
# os.system('ps aux') # Плохой способ


# Запуск сторонни приложений
# Рекомендуется


import subprocess, time, sys

text = subprocess.check_output(['ps', 'aux'], shell=True) # tasklist

for line in text.split(b'\n'):
    if b'python' in line:
        lst = line.decode().split()
        print( lst[5], lst[10] )




