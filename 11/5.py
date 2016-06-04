
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

    data = conn.recv(1024)
    ## посчитать
    ##

    print('getted:', data)
    
    if not data:
        return False

    data = data.decode('utf-8')

    # 10;20;+
    a, b, operation = data.split(';')

    result = calc(int(a), int(b), operation)

    # отправить результат
    #
    result = 'result: {}'.format(result).encode('utf-8')
    print(result)
    conn.sendall(result)
    return True


def calc( a, b, operation ):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b


if __name__=='__main__':

    serve('', 50008)