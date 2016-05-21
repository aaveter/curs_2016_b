# coding: utf-8
with open('file.txt') as f:

    lst = f.read().split(';')

    # Генератор списка (создание списка через выражение)
    lst = [ int(s) for s in lst ] # преобразуем элементы в числа


    #lst = list( map(int, lst) )
    #print( lst )


    mxn, mnn, summa = max(lst), min(lst), sum(lst)

    print('mxn: {}, mnn: {}, summa: {}'.format(mxn, mnn, summa))
