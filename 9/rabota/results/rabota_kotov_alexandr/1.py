n = 0

def smart_task():
    global n                                            ## +
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_1, param_2 ):                     ## ++
    if param_1 == None:
        return None
    print( " task "+ other_task.__name__ + " start")    ## +
    for p in param_1:
        count = param_2.count(p)
        print("\t- count of 'p': ", count)              ## ++
    print(" task " + other_task.__name__ + " stop")     ## +

smart_task()
smart_task()

other_task(('3', '4'), str(325543523))

smart_task()