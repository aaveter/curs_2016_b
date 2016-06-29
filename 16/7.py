


class A:

    @staticmethod
    def okay():
        print('okay!')

    @classmethod # Метод класса
    def not_okay(cls):
        print('not okay from class:', cls)

    @classmethod
    def create(cls):
        return cls() # создание такого же экземпляра


# A.okay()
# A.not_okay()

a = A()
b = A.create()


# ==================================================
from abc import ABC, abstractclassmethod, abstractproperty, abstractstaticmethod


class Base(ABC):

    @abstractstaticmethod
    def all_names():
        pass

    @abstractclassmethod
    def create(cls):
        pass

    @abstractproperty
    def name(self):
        pass


class Student(Base):

    __names = []

    def __init__(self, name=None):
        self.__name = name
        Student.__names.append(name)

    @staticmethod
    def all_names():
        return Student.__names

    @classmethod
    def create(cls):
        return cls()

    @property
    def name(self):
       return self.__name


s = Student('Max')
print( 'names:', Student.all_names() )
print( s.name )


b = s.create()
print( b.name )

