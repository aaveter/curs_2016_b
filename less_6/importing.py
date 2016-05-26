

import os

#print( dir(os) )

if not os.path.exists('ttt/lll/356'):
    os.makedirs('ttt/lll/356') # рекурсивное создание создание папок до пути



import math

print( math.cos(90) )





from math import (sqrt, cos,
                  sin, tan)


print( sqrt(4) ) # квадратный корень
print( sin(30) )


from datetime import datetime

datetime.now()


#from datetime.datetime import now

from os.path import exists

exists('.')


# если мы находимся в папке 'less_6'
import some_module

# если мы на уровень выше
from less_6 import some_module

some_module.some_func()


# Если мы находимся в папке 5



from less_6 import some_module


import sys
print(sys.path)

sys.path.append('../')

# выход на уровень выше для импортирования
from less_6 import some_module

