html = '''
<html>
    <body>
        <p>Some text..</p>
        <ul id='some_list'>
            <li>Ненужный элемент</li>
        </ul>
        <p>Some text..</p>
        <ul id='menu'>
            <li>Изделия</li>
            <li>Функциональность</li>
            <li>История</li>
            <li>Конфигуратор</li>
        </ul>
    </body>
</html>
'''

def foo():

    a = html.find("<ul id='menu'>")
    # нахожу начало меню
    # затем просто делаю срезы по индексам <li>
    # и затем делаю список из этих срезов
    #
    не успел







