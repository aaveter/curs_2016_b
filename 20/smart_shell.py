# coding: utf-8

# Напишите программу в ООП стиле.
#
# В бесконечном цикле программа ждет команд извне: из сокета
# или из командной строки.

# По типу команды запускается нужный режим. Команды: текущее время,
# свободное место и список файлов.

# В режиме “Список файлов” пользователю также предлагается: вывести
# список файлов, создать файл, удалить, а так же архифировать.

# При старте архивации общение с программой продолжается,
# а по завершению архивации, пользователь информируется об этом.

import os, datetime, subprocess
from time_work import TimeGetter

class IOBase:
    pass

class FilesGetter:

    def execute(self):
        pass


class Contoller:

    def __init__(self, commands):
        self._commands = commands

    def execute(self, argv=[]):
        while True:
            com = input(u'Введите команду:')
            if not self.try_command(com): # проверка команды
                print(u'Неверная команда: {}, продолжение.'.format(com))

    def try_command(self, com):
        if com in self._commands:
            self._commands[com].execute()
            return True


con = Contoller({
    'files': None,
    'time': TimeGetter(),
})