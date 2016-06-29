
from abc import ABC, abstractmethod

# (шаблон "Интерфейс")

class DataBase(ABC):

    @abstractmethod
    def connect(self, source, password=None):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self, sql):
        pass


# d = SomeBase()
# d.connect('127.0.0.1', password='vfdvfd')
# d.execute('select * from students;')
# d.close()

import os, json

class JsonBase(DataBase):

    def connect(self, source, password=None):
        #if os.path.exists(source):
        self._source = source
        self._data = json.load(open(source))

    def close(self):
        json.dump(self._data, open(self._source, 'w'))

    def execute(self, sql):
        command = sql.split()
        if command[0] == 'select':
            if command[1] == '*':
                if command[2] == 'from':
                    return self._select_table(command[3])

    def _select_table(self, name):
        #print( 'name:', name, name == 'students' )
        if not name in self._data:
            return []
        return self._data[name]



j = JsonBase()
j.connect('students.json')
students = j.execute('select * from students')

#print(j._data)

print( students )