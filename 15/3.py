

class SomeClass:

    def __getattr__(self, item):
        print('.')
        return u'У меня нет такого аттрибута: {}'.format(item)


s = SomeClass()


print( s.say_hello )
print( s.StartTrek )



s.say_hello = 30
print( s.say_hello )
print( s.StartTrek )



class UsersClass:

    _users = {'admin': '1234'}

    Galya = 667

    def __setattr__(self, key, value):
        if key != 'admin':
            self._users[key] = value

    def __getattr__(self, item):
        if item != 'admin':
            return self._users[item]


users = UsersClass()
users.Alex = 'b3467b'
users.Monika = 'vc6737cbg'

print( users.Alex )
users.admin = '111'
print( users.admin )
print( users._users )

users.Galya = 668
print( users.Galya )
print( users._users )

# -------------------------------

class UsersClass2:

    _users = {'admin': '1234'}

    Galya = 667

    def __setattr__(self, key, value):
        if key != 'admin':
            self.__dict__[key] = value

    def __getattribute__(self, item):
        if item != 'admin':
            return self._users[item]


users = UsersClass2()
users.__dict__['Zshenya'] = 567

print( users.Zshenya )



class SomeClass:
    name = 'vchdjsvhj'

    def some_method(self):
        pass


s = SomeClass()
print( '\n'.join(dir(s)) )
print( SomeClass.__dict__ )


