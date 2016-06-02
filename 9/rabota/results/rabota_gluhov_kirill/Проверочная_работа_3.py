# 3. Написать функцию, которая...

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

# найдет в тексте html пункты меню и сделает список с их названиями

## +++

def find_menu( text ):
    a_text = text.split()
    for word in a_text:
        if "li" in word and ( a_text.index( "id='menu'>" ) < a_text.index(word) > a_text.index( "</ul>" )):
            print( word[4:-5] )
        elif int( a_text.index( word )) > int(a_text.index( "id='menu'>" )):
            break


find_menu( html )