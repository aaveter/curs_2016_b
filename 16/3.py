

class Utka:

    def golos(self):
        return 'krya-krya'

class Dog:

    def golos(self):
        return 'gwow-gwow'

class Selezen:

    def golos(self):
        return 'krya-krya'



d = Dog()
u = Utka()
s = Selezen()

animals = [d, u, Dog(), Dog(), s]


for a in animals:
    print( a.golos() )


print( u'является ли селень уткой:', s.golos() == u.golos() )
print( u'является ли собака уткой:', d.golos() == u.golos() )
