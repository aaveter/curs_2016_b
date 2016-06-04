


# Echo server program
import socket

HOST = ''    # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

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
            while True:

                data = conn.recv(1024)

                ## посчитать
                ##

                print('getted:', data.decode('utf-8'))
                if not data:
                    break


                # отправить результат
                #
                conn.sendall(data)
