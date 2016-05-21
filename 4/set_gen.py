


# Генератор множества (ОСТОРОРОЖНО python 3)


# s = { -a/2.0 for a in range(10) }
#
# print( s )


lst = [1, 20, 3, 1, 1, 1]

# s = { a*2 for a in lst if a < 10 }
#
# print( s )
#
#
# lst = [ a*2 for a in lst if a < 10 ]
# print( lst )


s = { a*2 if a < 10 else -a for a in lst }
print( s )

















