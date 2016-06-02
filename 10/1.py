

# @autorized
# def func():
#     pass
#
# hasattr(func, 'some_attr')
#
#
#
# @runnable
# def func():
#     pass



import sqlite3

# Данных
# Базы Данных
# SQL - язык работы с данными
# sqlite - версия / отдельная база данных


# Таблица "Люди"

#   id   |     Имя     |    Возраст    |
#   0    | Max         | 16
#   1    | Olga        | 41


# Создаем объект соединения
with sqlite3.connect('try_slite.db') as con:
    # выполнить команду SQL
    #try:
    con.execute('create table IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name varchar(100), age int)')
    #except sqlite3.OperationalError:
    #    pass

    # добавляем строку в таблицу

    def insert_man(name, age):
        con.execute("insert into people (name, age) values (?, ?)", (name, age))

    insert_man(name='Vitaly', age=48)

    r = con.execute("select * from people")

    for a in r:
        print(a)
