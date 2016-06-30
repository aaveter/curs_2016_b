
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
                             QHBoxLayout, QPushButton, QMessageBox,
                             QTableWidget, QTableWidgetItem)

import xlrd, xlwt, os

class Table(QWidget):


    def __init__(self):
        super().__init__()

        self.lay = QHBoxLayout(self)
        self.tableWidget = QTableWidget(self)

        self.lay.addWidget(self.tableWidget)

        for i in range(2):
            self.tableWidget.insertRow(i)
            self.tableWidget.insertColumn(i)

        for i in range(2):
            for j in range(2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(''))

        # self.tableWidget.setItem(int row, int column, QTableWidgetItem *item)
        # self.tableWidget.takeItem(int row, int column)

        self.load()

    def load(self):
        if os.path.exists('temp.xls'):
            # открываем файл
            rb = xlrd.open_workbook('temp.xls', formatting_info=True)

            # выбираем активный лист
            sheet = rb.sheet_by_index(0)

            # получаем список значений из всех записей
            # vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

            rows = self.tableWidget.rowCount()
            cols = self.tableWidget.columnCount()

            print(':', rows, cols)

            for rownum in range(rows):
                row = sheet.row_values(rownum)
                for col in range(cols):
                    print(rownum, col)
                    item = self.tableWidget.item(rownum, col)
                    item.setText(row[col])

    def save(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Test')

        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()

        for row in range(rows):
            for col in range(cols):
                item = self.tableWidget.item(row, col)
                ws.write(row, col, item.text())

        # сохраняем рабочую книгу
        wb.save('temp.xls')

    def closeEvent(self, event):
        print('saving...')
        self.save()
        return super().closeEvent(event)