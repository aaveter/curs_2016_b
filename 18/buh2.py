# coding: utf-8

try:
    from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
                                 QHBoxLayout, QPushButton, QMessageBox,
                                 QTableWidget)
except ImportError:
    from PyQt4.QtGui import QWidget, QApplication

from buh1 import User
from table import Table
import time

app = QApplication([])

w = QWidget() # базовый класс всех окон

lay = QHBoxLayout(w) # сразу подключаем лэйаут к виджету w


def login(*args):
    global w
    name = w.loginEdit.text()
    password = w.passwordEdit.text()

    if User.login(name, password):
        ret = QMessageBox.question(w, 'Приветствие', 'Ура, Вы вошли!',
                                   QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            w = Table()
            w.show()


w.loginEdit = QLineEdit(w)
w.loginEdit.setPlaceholderText('Имя')

w.passwordEdit = QLineEdit(w)
w.passwordEdit.setPlaceholderText('Пароль')
w.passwordEdit.setEchoMode(QLineEdit.Password)

w.loginButton = QPushButton(w)
w.loginButton.setText('Войти')
w.loginButton.clicked.connect(login) # подсоединяем 'слот' к 'сигналу'


lay.addWidget(w.loginEdit)
lay.addWidget(w.passwordEdit)
lay.addWidget(w.loginButton)


w.show()

app.exec_()