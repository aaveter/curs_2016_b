

users = [
    'user1',
    'user2',
    'user3',
]


users.append('user3')
print( users )


users_set = set( users )
users = list( users_set )
users.sort(reverse=False)

print( users )


s = {1, 2, 3}
s2 = {3, 4, 5}

print( s2.difference(s) )
print( s2.intersection(s) )
print( s2.issubset({3, 4, 5, 6}) )

print( s2.union(s) )