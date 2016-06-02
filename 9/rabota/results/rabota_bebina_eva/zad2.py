# 2. Дополнить функциональность:

names = ('Мария{}', 'Григорий{}', 'Максим{}')

for name in names:
    length = len(name)
    glasniye = len( [sym for sym in name.lower() if sym in 'йуеыаоэё'] )
    procent = glasniye / length

print( 'Процент гласных в словах следующий:','procent )

for name in procent:
    print( '\t{}: {}%'.format(name, procent[name]) )