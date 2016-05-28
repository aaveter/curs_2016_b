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
    try:
        con.execute('create table people (id int, name varchar(100), age int)')
    except sqlite3.OperationalError:
        pass

    # добавляем строку в таблицу
    #con.execute("insert into people (id, name, age) values (2, 'Olga', 41)")

    # выборка из таблицы
    # for a in con.execute("select * from people"):
    #      print( a )


    # r = con.execute("select * from people")
    # print( r )

    # Так можно получить курсор:
    # cur = con.cursor()
    # cur.execute()

    # Выборка с условием
    for a in con.execute("select * from people where age > ? and name like ?", (40, 'O%') ):
        print( a )
