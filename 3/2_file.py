import os

if os.path.exists('1.py'):

    # Менеджер контекста
    with open('1.py', encoding='utf-8') as f:

        with open('333.py', 'a') as g:

            g.write('\n' + f.read())