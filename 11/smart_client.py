
import socket

# Создаем объект сокета
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TCP+IP соединение, потоковый

# Устанавливаем таймаут
s.settimeout(3)

# Соединяемся с сервером
s.connect(('192.168.7.102', 50007))# "www.python.org", 80))


data = b'''GET / HTTP/1.1

'''

data = u'Привет всем!'.encode('utf-8')

# Отправляем
s.sendall(data)

# Читаем данные
data = s.recv(100)

print( data )