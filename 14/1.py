
# Свойства

class Point:

    def set_x(self, value):
        print( 'log: set x {}'.format(value) )
        self._x = value

    def set_y(self, value):
        print('log: set y {}'.format(value))
        self._y = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


p1 = Point()
p1.set_x(20)
p1.set_y(40)


print( p1._x, p1._y )


# ===================================

class Point:

    _x = 10
    _y = 20

    @property
    def x(self):
        print( 'User get x!!!!' )
        return self._x

    @property
    def y(self):
        print('User get y!!!!')
        return self._y


p = Point()
print( p.x, p.y )

p.x = 100 # Error !!! Нельзя задать свойство


# ===================================

class Point:

    __x = 10
    __y = 20

    @property
    def x(self):
        print( 'User get x!!!!' )
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise Exception(u'Задавай x типа int!!!')
        self.__x = value

    @property
    def y(self):
        print('User get y!!!!')
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @x.deleter
    def x(self):
        self.__x = 0

p = Point()
print( p.x, p.y )

#print( p._Point__x )

print( dir(p) )

del p.x # Error без x.deleter
#p.x = 100

print( p.x, p.y )




p.x = 10
print( p.x )



class Dog( Animal ): # наследование

    owner = None # Добавка

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    @property
    def day_corm_limit(self):
        return self.weight * self.age

lessy = Dog(age=7, weight=20)
lessy.owner = SomeOwner('Max')
print( lessy.day_corm_limit )





