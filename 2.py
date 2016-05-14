
# Кортеж | неизменяемый
# - скорость создания
# - экономия памяти

perem = 6

lst = [12, 16]
s = 'Alex'

k = (s, 'Ivanov', perem, lst)


num = len(k) # кол-во эелементов k


print( k )


perem = 12
lst.append(100)
s += '________'


print( k )


# Строка | неизменяемая