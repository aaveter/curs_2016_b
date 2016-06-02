names = ['Мария', 'Григорий', 'Максим']
procents = []                                                               ## +
for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'уеыаоэёюяи' ])  ## +
    procent = int((glasniye / length)*100)
    procents.append(procent)                                                ## +

print( 'Процент гласных в словах следующий:' )
i = 0
for name in names:
    print( '\t{}: {}%'.format(name, procents[i]) )
    i+=1