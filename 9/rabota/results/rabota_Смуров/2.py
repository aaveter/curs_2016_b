# 2. Дополнить функциональность:
procents = {}                                   ## +
names = ('Мария', 'Григорий', 'Максим')
for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'йуеыаоэё' ])
    procent = glasniye / length
    procents[name] = str(procent)               ## +
print( 'Процент гласных в словах следующий:' )

for name in procents:
    print( '\t{}: {}%'.format(name, procents[name]) )
