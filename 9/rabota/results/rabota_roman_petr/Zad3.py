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
list = []
html_manipulate = html.split("<ul id='menu'>")
html_manipulate = html_manipulate[1].split('</ul>')
html_manipulate = html_manipulate[0].split('\n')
for line in html_manipulate:
    line = line.strip()
    if line != '':
        list.append(line)
# cutting_edge = html_manipulate.index("</ul>")
# menu_RAW = html_manipulate[:cutting_edge]
print(list)

## ++ осталось сделать из этого функцию и от li избавиться =)
## реализация опасная!


# найдет в тексте html пункты меню и сделает список с их названиями