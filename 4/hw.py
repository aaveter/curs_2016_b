


with open('file.txt') as f:

    # 1.
    data = f.read()
    lst = data.split(';')

    # 2.
    summa = 0
    for sym in lst:
        summa += int(sym)
    print('summa:', summa)

    # 3.
    mnn, mxn = int(lst[0]), int(lst[0])
    for sym in lst:
        sym = int(sym)

        if sym < mnn:
            mnn = sym

        if int(sym) > mxn:
            mxn = sym

    print(lst)
    print('min:', mnn, 'max:', mxn)


