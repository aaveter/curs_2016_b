




def counter(preffix, n):

    some_lamb = lambda : None

    for a in range(n):
        yield some_lamb, a



for preffix, a in counter(preffix='buy', n=3):
    print(preffix, a)

for preffix, a in counter(preffix='buy', n=3):
    print(preffix, a)