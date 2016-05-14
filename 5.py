# coding: utf-8

people = {
    #имя фамилия рост кол-во дет
    'Bob': ['Guns', 182, 3],
    'marly': ['vendy', 167, 2]
}

sum_rost = 0
for name in people:

    man_info = people[name]
    rost = man_info[1]

    sum_rost += rost


print (u'Средний рост:', sum_rost / len(people))





#rost__ = list( people.keys() )[2]