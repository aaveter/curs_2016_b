import pickle


# pickle - НЕ ЗАЩИНЕН



TREE = pickle.load(open('read_write.data', 'rb'))


print( TREE )