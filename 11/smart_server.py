import os

# 1) запрос "имени файла" --> ответ да/нет

# 2) запрос части с 3000 байта до 4000 байта

# 3) скачивание этой части файла...


# Echo server program
import socket

def serve(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Резервируем адрес и порт в системе
        s.bind((HOST, PORT))

        # Ждать соединений
        s.listen(1) # одновременных соединений может быть не больше 1

        while True:
            # Принимаем соединение
            conn, addr = s.accept() # Объект соедиени, адрес (откуда)

            with conn:
                print('Connected by', addr)
                while handle(conn):
                    pass


def handle(conn):

    filename = conn.recv(1024).decode('utf-8')

    if not filename:
        return False

    # Принимаем имя файла и отвечаем, есть ли

    if os.path.exists(filename):
        size = os.path.getsize(filename) # Получаем размер файла
        conn.sendall('exists;{}'.format(size).encode('utf-8'))
    else:
        conn.sendall(b'no')
        return False

    data = conn.recv(1024).decode('utf-8')

    # Принимаем запрашиваемую часть файла
    a, b = data.split(";")
    start, end = int(a), int(b)

    # Открываем файл и сдвигаемся на start
    with open(filename, 'r+b') as f:

        print('start sending...')

        f.seek(start)
        data = f.read(end-start)
        conn.sendall(data)

        print('fin, sended {} bytes'.format(end-start))

    return True


if __name__=='__main__':

    serve('', 50008)

