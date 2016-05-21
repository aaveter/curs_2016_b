
# контекстный менеджер
with open('user.txt') as f:

    for line in f:

        print (line.strip()) # удаляем пустоты слева и справа строки

        #print (line, end='')

# <------- файл закрывается