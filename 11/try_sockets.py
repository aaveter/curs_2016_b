

import socket

# Создаем объект сокета
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем таймаут
s.settimeout(3)

# Соединяемся с сервером
s.connect(('localhost', 50007))# "www.python.org", 80))


data = b'''GET / HTTP/1.1

'''

# Отправляем
s.sendall(data)

# Читаем данные
data = s.recv(100)

print( data )