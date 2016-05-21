

# # про список
# if "hello" in s:
#     s.append('buy')



lst = [1, 2, 3]

#print( str(lst) )

lst_2 = []
for sym in lst:
    sym = str(sym)
    lst_2.append(sym)


lst_2 = set(lst_2)

s = ';'.join(lst_2)
print(s)

#s = '1;2;3'







x = 0
for i in range(12):

    for j in range(20):
        x += i * j

        if j > x > i:
            continue

        elif x == i == j:
            print('OK!!!')

        print(x)







