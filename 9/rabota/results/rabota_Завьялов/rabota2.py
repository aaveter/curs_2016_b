#coding: utf-8
names = ('Мария', 'Григорий', 'Максим')
procents={}                                                                 ## +
for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'йуеыаоэё' ])
    procent = glasniye / length
    procents[name]=procent                                                  ## +
print( 'Процент гласных в словах следующий:' )

for name in procents:
    print( '\t{}: {}%'.format(name, procents[name]) )
