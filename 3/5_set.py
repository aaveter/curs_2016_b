# Множество



s = { 1, 3, 20, 'ghg' }

#s = set() # пустое

s.add( 30 ) # добавление

#dlina = len( s )


s.add( 20 )

#print ( s )


set( list( s ) )


s2 = {0, 'Hello', 3}

s.update(s2) # добавление элементов из второго множества

for a in s:
    print (a)


