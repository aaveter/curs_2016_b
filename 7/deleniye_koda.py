
# 2. сделать программу калькулятор
# вечный цикл
# вычисление того, что получили через input (первый input - 2 числа, второй - знак операции)
# EXIT - выход из программы

def calc( a, b, operation ):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b

while 1 == 1:
    enter_1 = [ i for i in input('Введите два числа, или "exit" для выхода: ').split() ]

    if 'exit' in enter_1:
        break

    enter_2 = [ i for i in input( 'Введите операцию над числами, или "exit" для выхода: ' ).split() ]

    if 'exit' in enter_2:
        break

    numbers = [ int(i) for i in enter_1 ]
    operation = enter_2[0]
    a, b = numbers
    print( 'Ответ: ', calc( a, b, operation ) )


