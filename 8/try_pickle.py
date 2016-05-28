import pickle

# Задача: при следующем запуске снова получать сохранять данные

PEOPLE = []

# Получаем список из бинарных данных
try:
    #with open('try_pickle.data', 'rb') as f:
    #    o = f.read()
    #    PEOPLE = pickle.loads(o)
    PEOPLE = pickle.load(open('try_pickle.data', 'rb'))
except FileNotFoundError:
    pass

#print( 'NEW PEOPLE:', PEOPLE )
for man in PEOPLE:
    name = man['name']
    zp = man['money']
    print('-- {} зарабатывает {} рублей в год'.format(
        name,
        zp
    ))

def get_input():
    return input(u'''Введите информацию о человеке:
    # Пример: Василий Рогов, 30000 рублей
    ''')

def parse(text):
    name, money_s = text.split(',')
    money = int(money_s.replace(u'рублей', ''))
    return {
        'name': name,
        'money': money
    }

text = get_input()

PEOPLE.append(
    parse(text)
)

# Сохраняем в объект = в бинарные данные
# o = pickle.dumps(PEOPLE)
# with open('try_pickle.data', 'wb') as f:
#     f.write(o)
pickle.dump(PEOPLE, open('try_pickle.data', 'wb'))

#print( 'PEOPLE:', o )
print('ok')
