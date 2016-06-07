#coding: utf-8
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

## +++ пойдет

# найдет в тексте html пункты меню и сделает список с их названиями
M=0
menu=[]
A=html.split('\n')
for i in A:
    if "<ul id='menu'>" not in i and M==0:
        continue
    elif "</ul>" in i:
        M=0
        continue
    else:
        if "<ul id='menu'>" in i:
            M+=1
        else:
            while "/" in i:
                i=i[:-1]
            i=i[:-1]
            while ">" in i:
                i=i[1:]
            #menu.append(i[16:-5])
            menu.append(i)
print(menu)



