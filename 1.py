# coding: utf-8

lst = [
    #имя фамилия рост кол-во дет
    ['Bob', 'Guns', 182, 3 ],
    ['marly','vendy', 167,2]
    ]

sum_children=0
average_h=0
sum_letter=0

# for i in range(len(lst)):
#     sum_children += lst[i][3]

for man in lst:
    sum_children += man[3]

    # if sum_children > 10:
    #     continue # пропуск того, что ниже  - к след итерации
    #
    # if sum_children > 5:
    #     break # выход

else:
    # сюда попадем, если break не было, то есть все элементы отрабтали
    print ('Попали сюда')

# Продолжаем
