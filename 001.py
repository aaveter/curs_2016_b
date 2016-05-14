# Список

lst = [1, 2, 3, 4, 5]
#lst = list()

# берем элемент по индексу
#print( lst[2] )

# lst[2] = 100
# lst[3] = 13
# lst[-2] = 13

#lst[2 : 4] = [1, 42, 43, 45]

# берем срез



del lst[3]
print( lst )

a = 'Hello'
del a

print (a)



# Кортеж

a = 100
b = 200
c = 300

a, b, c = b, c, a

print (a, b, c)


hello = 10, 10, 30, 550

print( type(hello) ) # получить тип переменной

pustoy = ('s') # Кортеж с 1 элементом преобразуется в сам элемент!!!!
print (type(pustoy))

pustoy = ('s',) # Так получится
print (type(pustoy))

pustoy = tuple('s')
print (type(pustoy))















