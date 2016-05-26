



def get_address():

    d = {
        'ip': 'masterhos.ru',
        'port': 3080
    }

    return d


address = get_address()

ip = address['ip']
port = address['port']



def get_address_2():
    return 'masterhos.ru:8030'

address = get_address_2()
_lst = address.split(':')
ip = _lst[0]
port = _lst[1]



def get_address_3():
    return 'masterhos.ru', 8030


ip, port = get_address_3()