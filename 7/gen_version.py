

def gen_operations():
    while True:
        enter_1 = input('Введите два числа, или "exit" для выхода: ').split()

        if 'exit' in enter_1:
            break

        enter_2 = input( 'Введите операцию над числами, или "exit" для выхода: ' ).split()

        if 'exit' in enter_2:
            break

        numbers = [ int(i) for i in enter_1 ]
        operation = enter_2[0]
        a, b = numbers

        yield a, b, operation


def main():
    def calc(a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b

    for a, b, operation in gen_operations():
        print('Ответ: ', calc(a, b, operation))

