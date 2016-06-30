# coding: utf-8

try:
    from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
                                 QHBoxLayout, QPushButton, QMessageBox,
                                 QTableWidget)
    import PyQt5
except ImportError:
    from PyQt4.QtGui import QWidget, QApplication

from buh1 import User
from table import Table
import time

app = QApplication([])

class LoginWidget(QWidget):

    def __init__(self):
        super().__init__()

        lay = QHBoxLayout(self)  # сразу подключаем лэйаут к виджету w

        self.loginEdit = QLineEdit(self)
        self.loginEdit.setPlaceholderText('Имя')
        self.loginEdit.installEventFilter(self) # делаем текущий виджет наблюдателем событий виджета loginWidget

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setPlaceholderText('Пароль')
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.installEventFilter(self) # делаем текущий виджет наблюдателем событий виджета passwordEdit

        self.loginButton = QPushButton(self)
        self.loginButton.setText('Войти')
        self.loginButton.clicked.connect(self.login)  # подсоединяем 'слот' к 'сигналу'

        lay.addWidget(self.loginEdit)
        lay.addWidget(self.passwordEdit)
        lay.addWidget(self.loginButton)

    def login(self, *args):
        global w
        name = w.loginEdit.text()
        password = w.passwordEdit.text()

        if User.login(name, password):
            w = Table()
            w.show()

    def eventFilter(self, watched, event):
        #print('eventFilter: {} - {}'.format(watched, event))
        return super().eventFilter(watched, event)

    def keyPressEvent(self, event):
        if event.key() in (
                PyQt5.QtCore.Qt.Key_Enter,
                PyQt5.QtCore.Qt.Key_Return): # FIXME найти тип
            print('-- ENTER --')
            self.login()


w = LoginWidget() # базовый класс всех окон
w.show()

app.exec_()