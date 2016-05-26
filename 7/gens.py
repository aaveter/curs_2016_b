

# Генераторы

lst = range(1000000) # создает список в python 2
lst = list(range(1000000)) # создадим список в python 3


lst[100] = 'hi!'


gen = range(1000000) # создает генератор в python 3

#lst = [0, 1, 2 ...., 999999]

#gen[100] = 'hi'


for a in gen:
    print( a )

# - не создают массив в памяти, а вычисляют новое значение в нужный момент


lst = [a for a in range(10) if a < 5] # генератор списка


gen = (a for a in range(10) if a < 5) # генератор, краткая запись


for a in gen:
    print( a )

#print( gen[1] )