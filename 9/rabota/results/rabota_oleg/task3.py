# coding: utf-8
import re
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

## +++ -- нужно было сделать функцию =)

# найдет в тексте html пункты меню и сделает список с их названиями
mbl=re.search("<ul\s+id='menu'.+?</ul>",html,re.DOTALL)
mi=re.findall('<li>(.+?)</li>',mbl.group(0))
print(mi)
