# coding: utf-8


# ------- PyQt4 --------

# - фрэйворк, библиотека
# - для оконных приложений !
# - работа с сетями, файлами, (списки, словари), сокеты...


import sys
from PyQt4 import QtGui



app = QtGui.QApplication([]) # объект приложения (СИНГЛТОН)

# Создаем главное окно
w = QtGui.QLabel('Hello from Qt!!!') # Строка текста
w.show() # Отобразить

sys.exit(app.exec_()) # запускаем приложение, а когда завершится, возвращаем код ошибки

## !!! loop events = событийная модель


