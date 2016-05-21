

# глобальная
GLOB = 'SOME GLOBAL'


def func():
    global GLOB # возможность редактирования глобальной переменной
    print(GLOB)

    GLOB = 'NEW GLOB'


func()
print('new GLOB:', GLOB)



# Области видимости:

GLOB = '2345t6'

def func2():

    x = 122
    y = 30

    print('local:', locals()) # возвращает словарь со значениями локальных переменных

    print('globals:', globals())

func2()




import os


path = os.path.abspath(__file__)
my_dir = os.path.dirname(path)
print( path )


#open(my_dir + "/some_file.txt")


#
if __name__=='__main__':
    # этот код будет выполнен если это глайный файл программы
    # когда python glob.py

    print("ZAPUSTILI!!!!")



