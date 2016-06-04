
import socket, os

IP_PREFFIX = '192.168.7.'


def get_filepart(ip, filename, start):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(0.3)

    try:
        s.connect((ip, 50008))
    except socket.error:
        return False

    # 1) Отправить имя файла
    s.sendall(filename.encode('utf-8'))

    answer = s.recv(1024).decode('utf-8')
    if not 'exists' in answer:
        return False
    ln = int(answer.split(';')[1])

    part_size = int(ln / 10)
    end = start + part_size

    print( 'file exists ({} bytes), getting part {}:{}...'.format(ln, start, end) )

    if end > ln:
        end = ln

    if end <= start:
        return None

    # отправляем начало и конец части
    s.sendall('{};{}'.format(start, end).encode('utf-8'))

    # Читаем часть из сокета
    part = s.recv(end-start)

    filename = filename.replace('.', '.out.')
    flag = 'r+b' if os.path.exists(filename) else 'wb'

    with open(filename, flag) as f:

        f.seek(start)
        f.write(part)

    s.close()

    print('part got')
    return end


def get_file(filename):
    start, end = 0, 0

    for a in range(100, 255):
        ip = IP_PREFFIX + str(a)
        print('try ip:', ip)

        # Получаем часть. Если не знали размер файла, то получаем и
        # вычисляем следующий start.
        ret = get_filepart(ip, filename, start)
        if not ret:
            if ret == None:
                print('all file got')
                break
            continue
        start = ret


if __name__=='__main__':

    get_file(filename='data/python.jpg')