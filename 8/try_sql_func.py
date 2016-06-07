
import sqlite3


def execute_sql(sql, params=()):
    # Создаем объект соединения
    with sqlite3.connect('try_slite.db') as con:
        # выполнить команду SQL
        try:
            con.execute('create table people (id int, name varchar(100), age int)')
        except sqlite3.OperationalError:
            pass

        r = con.execute(sql, params)



execute_sql('select * from people')

execute_sql('insert...')