def smart_task(n = 0):                                              ## ++ хотя и не совсем логично
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task(param_1, param_2):                                   ## ++
    if param_1 == None:
        return None
    print( " task other_task start")                                ## + один на две строчки)
    for p in param_1:
        print("\t- count of 'p': " + str(len(str(param_2))))        ## +
    print(" task other_task  stop")

smart_task()
smart_task()

other_task(('3', '4'), str('325543523'))

smart_task()
