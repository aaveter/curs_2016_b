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

## ++ за наглость =)

html1 = html.split('\n')
for line in html1:
      if line != '<li>Ненужный элемент</li>':
          if '<li>' in line:
               print(line)
