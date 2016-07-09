# coding: utf-8
import datetime

class TimeGetter:

    def execute(self):
        print(u'Текущее время: {}'.format(datetime.datetime.now()))