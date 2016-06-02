# coding: utf-8


# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')
procent = []																## +

for name in names:
	length = len(name)
	glasniye = len([ sym for sym in name.lower() if sym in 'ауоыиэяюёе' ])	## +
	procent.append(glasniye / length *100);									## +
	

print( 'Процент гласных в словах следующий:' )

i=0;																		## -
for name in names:
	print( '\t{}: {}%'.format(name, procent[i]) )
	i+=1
