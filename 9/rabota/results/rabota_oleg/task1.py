# coding: utf-8

# 1. Исправить ошибки в этом программном коде
import sys

n = 0

def smart_task():
	global n                                                                ## +
	n += 1
	print( 'start of ',sys._getframe().f_code.co_name,' #{}'.format(n) )    ## +

def other_task(param_2,param_1=None):                                       ## ++
    if param_1 == None:
        return None
    print( " task ",other_task.__name__," start")                           ## +
    for p in param_1:
        print("\t- count of '",str(p),"': " + str(param_2.count(p)))        ## ++
    print(" task ",other_task.__name__," stop")                             ## +

smart_task()
smart_task()

other_task(str(325543523),('3', '4'))

smart_task()
