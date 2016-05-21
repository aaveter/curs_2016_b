
lst = [1, 2, 3]
lst2 = [10, 20, 30]


lst3 = []
summ_i = 0
for i in lst:
    summ_i += i
    for j in lst2:
        lst3.append(i + j) # добавляет элемент


# Вложенный генератор списка
lst4 = [i + j for i in lst
              for j in lst2 ]

# ! работает быстро

print( lst3 )
print( lst4 )