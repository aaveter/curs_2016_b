# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task(n):                                      ## +-
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_1=None, param_2=None ):           ## ++

    if param_1 == None:
        return None
    print( " task ", other_task.__name__, " start" )    ## +

    for i in param_1:
        print("\t- count of 'i': " + param_2.count(i))  ## ++

        print(" task ", other_task.__name__, " stop")   ## +

smart_task(1)
smart_task(2)

other_task(('3', '4'), str(325543523))

smart_task(3)