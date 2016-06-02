# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task():
    global n                                                        ## +
    n += 1
    print( 'start of smart_task #{}'.format(n) )

def other_task(param_1, param_2):                                   ## ++
    if param_1 == None:
        return None
    if param_2 == None:
        return None

    print("task {} start".format(other_task.__name__))              ## +
    
    for p in param_1:
    	c = 0
    	for s in param_2:
    		if s == p:
    			c += 1
    	print ("{} count of {} is {}".format(p, str(c), param_2))   ## ++   str не нужно; вроде перепутаны?
	print("task ", other_task.__name__," stop")                     ## +

smart_task()
smart_task()

other_task(('3', '4'), str(325543523))

smart_task()