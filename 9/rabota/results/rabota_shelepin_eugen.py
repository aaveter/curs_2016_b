# coding: utf-8

# 1. Исправить ошибки в этом программном коде

n = 0

def smart_task():
    global n                                                    ## +
    n+=1
    print( 'start of smart_task #{}'.format(n) )

def other_task( param_2, param_1=None  ):                       ## ++
    if param_1 == None:
        return None
    print( " task ",other_task.__name__," start")               ## +
    for p in param_1:
        print("\t- count of '",p,"': ", + param_2.count(p))     ## ++
    print(" task ",other_task.__name__," stop")                 ## +

smart_task()
smart_task()

#other_task[('4','3'), str(325543523)]
other_task('4','3')
smart_task()

# 2. Дополнить функциональность:
procents = 0
names = ('Мария', 'Григорий', 'Максим')
def glasnye(names):
 for name in names:
 length = len(name)                                                     ## ? табуляция
 glasniye = len([sym for sym in name.lower() if sym in 'йуеыаоэё'])
 procents = glasniye / length
 procents = int(round(procents, 2) * 100)                               ## ++
 yield name,procents,
gen=glasnye(names)
for a in gen:
 print ('\t{}: {}%'.format(a[0],a[1]))                                  ## ++
 procents=a[1]+procents

print( 'Процент гласных в словах следующий:',procents )
