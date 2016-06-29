

class A:

    __secret = 'cdbh^^c43cbjhd'

    def __getattribute__(self, item):
        if item == '_A__secret':
            #return None
            raise Exception('No attribute _A__secret')
        try:
            a = super().__getattribute__(item)
        except AttributeError:
            a = None
            setattr(self, item, a)
        return a


a = A()
print( a.ttt )

print( a._A__secret )