
from abc import abstractmethod, ABC

# Абстрактный класс


class Tranport(ABC): # наследуемся и делаем класс абстрактным

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def cacl_way(self):
        pass


class Car(Tranport):

    def run(self):
        pass

    #def cacl_way(self):
    #    pass


c = Car()