

# Генератор словаря (ОСТОРОРОЖНО python 3)


# lst = [1, 2, 3]
#
# d = { key: key*2 for key in lst }
#
# print( d )


students = [
    'Max:30',
    'Ulya:20',
]
lst = [ stud.split(':') for stud in students ]

d_students = { stud[0] : int(stud[1]) for stud in lst }

print( d_students )