

a = 0

if a > 10:
    a = -a
else:
    a = a


a = 0
a = 'BOLSHE' if a > 10 else 'MENSHE'
print( a )


a = 20
a = a > 10 and 'BOLSHE' or 'MENSHE' # !!!
print( a )