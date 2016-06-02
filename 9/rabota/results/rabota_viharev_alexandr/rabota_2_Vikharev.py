# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')

length = 0
glasniye = 0
procent = 0

for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'йуеыаоэё' ])
    procent = (glasniye / length) * 100                                     ## +-

print( 'Процент гласных в словах следующий:' '{}%'.format(procent) )

procents = ['']

for name in procents:

    print( '\t{}: {}%'.format(name, procents[name]) )                       ## ?