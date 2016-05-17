
text = '''

Hello, Bill!!

Send    me some info about lesson.

'''

words = text.split()

lev_syms = [ ',', '!', '.' ]

for word in words:
    if 'i' in word or 'o' in word:

        # if len(word) > 2:
        #     word = word[:3]

        # for sym in lev_syms:
        #     word = word.replace(sym, '')

        for sym in lev_syms:
            while sym in word:
                word = word[:-1]

        print( word )








#print( type(words) )

#print( len( words ) )






# ''.split(<делитель>)     ''.split()


