

from datetime import datetime


def func():
    func.last_call = datetime.now()


func()

# gg = globals()
# for g in gg:
#     print( g )

print( func.last_call )


# Рекурсия

import math
print( math.factorial(5) )

# 1 * 2 * 3 * 4 * 5

def factor(num):

    if num < 1:
        return 1

    # рекурсия
    return factor(num-1) * num


print( factor(5) )



import os

#os.chdir('less_6')

lst = ['a', '1']
lst.sort() #lst = sorted(lst)

def listing(path):
    filenames = os.listdir(path)
    print(filenames)
    for fi in sorted(filenames):
        if fi == '.idea':
            continue
        fileway = os.path.abspath(os.path.join(path, fi))

        if os.path.isdir(fileway) and fi[0]!=".":
            print('DIR:', fileway)
            listing(fileway)
        elif os.path.isfile(fileway):
            print(fileway)


listing(path='.')

# 1. отсортировать вывод на экран по алфавиту
# 2. не заходить в папку .git и другие, начинающиеся на .

import os

lst = []

def listing(path):
    filenames = os.listdir(path)
    for fi in filenames:
        fileway = os.path.abspath(os.path.join(path, fi))

        if os.path.isdir(fileway) and fi[0]!=".":
            #print('DIR:', fileway)
            listing(fileway)
            lst.append(fileway)
        elif os.path.isfile(fileway):
            #print(fileway)
            lst.append(fileway)

# listing(path='.')
#
# lst = sorted(lst)
# for i in lst:
#     print( i )