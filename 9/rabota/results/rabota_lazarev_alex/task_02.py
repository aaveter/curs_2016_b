# coding: utf-8

# 2. Дополнить функциональность:

names = ('Мария', 'Григорий', 'Максим')
procent = {}                                            ## +
procent2 = {}

for name in names:
    length = len(name)
    glasniye = len([ sym for sym in name.lower() if sym in 'йуеыаоэё' ])
    soglasniye = len([ sym for sym in name.lower() if sym in 'цкнгшщзхъфвпрлджчсмтьб' ])    ## + действительно дополнение функциональности =)
    
    p = glasniye / length
    p2 = soglasniye / length

	procent[name] = p                                   ## +-  табуляция
	procent2[name] = p2

print('Процент гласных в словах следующий:')

for name in glasniye:
    print( '\t{}: {}%'.format(name, procents[name]) )   # имя словаря другое..

print('Процент согласных в словах следующий:')

for name in procents2:
    print('\t{}: {}%'.format(name, procents2[name]))