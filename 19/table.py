
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
                             QHBoxLayout, QPushButton, QMessageBox,
                             QTableWidget)


class Table(QWidget):


    def __init__(self):
        super().__init__()

        self.lay = QHBoxLayout(self)
        self.tableWidget = QTableWidget(self)

        self.lay.addWidget(self.tableWidget)

        for i in range(20):
            self.tableWidget.insertRow(i)
            self.tableWidget.insertColumn(i)

        # self.tableWidget.setItem(int row, int column, QTableWidgetItem *item)
        # self.tableWidget.takeItem(int row, int column)