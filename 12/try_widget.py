# coding: utf-8


import sys
from PyQt4 import QtGui



app = QtGui.QApplication([]) # объект приложения (СИНГЛТОН)

# Создаем главное окно
w = QtGui.QWidget() # пустой виджет ( = форма = окно )

label = QtGui.QLabel(parent=w)
label.setText('Hello from Label on Widget')

button = QtGui.QPushButton(parent=w)
button.setText('+')

edit = QtGui.QLineEdit(w) # строка редактирования
edit_2 = QtGui.QLineEdit(w)

## Сигналы и Слоты (просто метод)

def on_clicked():
    #print('clicked!!!')
    a = int(edit.text())
    b = int(edit_2.text())
    summa = a + b

    label.setText(str(summa)) # берем текст из LineEdit

button.clicked.connect(on_clicked) # срабатывает по нажатию


button.move(30, 100) # сдвигаем кнопку вниз и вправо
edit.move(30, 70)
edit_2.move(200, 70)

w.show() # Отобразить
w.raise_() # для мака в PyQt4

sys.exit(app.exec_())