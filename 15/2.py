


class Name:
    pass



a = Name()
b = Name()


#c = a + b

c = 17 + 20
c = 'vfdv' + 'vfdvfd'


# Переопределение операторов



class Distance:

    def __init__(self, meters):
        self._meters = meters

    def __add__(self, other):
        self._meters += other._meters
        return self



r1 = Distance(100) # в результате изменим на 600
r2 = Distance(500)


r3 = r1 + r2
print( r3._meters )
print( r1, r3 )



# ПРАВИЛЬНО:

class Distance:

    def __init__(self, meters):
        self._meters = meters

    def __add__(self, other): # Сложение
        # Создаем новый экземляр класса
        d = Distance( self._meters + other._meters )
        return d

    def __sub__(self, other): # Вычитание
        pass

    def __mul__(self, other): # Умножение
        pass

    def __divmod__(self, other): # Деление
        pass

r1 = Distance(100) # в результате изменим на 600
r2 = Distance(500)

r3 = r1 + r2
print( r3._meters )
print( r1, r3 )


lst = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst + lst2
lst3 = lst - lst2

print( lst3 )



# Свой собственный улучшенный список


class SmartList(list):

    def __sub__(self, other):
        for a in other:
            self.remove(a) # удаляем первое вхождение элемента
        return self


lst1 = SmartList([1, 2, 3, 4])
lst2 = SmartList([2, 3])

lst3 = lst1 - lst2
print( id(lst1), id(lst3) ) # выводим адрес в памяти на объект



class SmartList(list):

    def __sub__(self, other):
        third = []
        for a in self:
            b = a in other
            if not b:
                third.append(a)
                #self.remove(a) # удаляем первое вхождение элемента
        return third


lst1 = SmartList([1, 2, 3, 4, 2])
lst2 = SmartList([2, 3])

lst3 = lst1 - lst2
print( id(lst1), id(lst3), lst3 ) # выводим адрес в памяти на объект


from collections import OrderedDict

o = OrderedDict({
    'b': 123,
    'a': 43234,
})

print( o )

