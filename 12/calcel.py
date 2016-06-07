# coding: utf-8
import sys
from PyQt4 import QtGui, uic


app = QtGui.QApplication([]) # объект приложения (СИНГЛТОН)

# Создаем главное окно
w = QtGui.QWidget() # пустой виджет ( = форма = окно )

uic.loadUi('calcer.ui', w)

def on_1():
    w.lineEdit.setText('1')

w.but_1.clicked.connect(on_1)

w.show() # Отобразить
w.raise_() # для мака в PyQt4

sys.exit(app.exec_())