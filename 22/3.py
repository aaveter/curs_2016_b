
html = '''
<html>
<body>
    <ul id='menu-1' style='color:red;'>
        <li>li 1</li>
        <li>li 2</li>
        <li>li 3</li>
    </ul>
    <ul id='menu-2'>
        <li>li 1</li>
        <li>li 2</li>
        <li>li 3</li>
    </ul>
</body>
</html>
'''


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    _menu_1 = False
    _menu_1_list = []
    _menu_1_li = False

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            for name, value in attrs:
                if name == 'id' and value == 'menu-1':
                    self._menu_1 = True
        elif tag == 'li' and self._menu_1:
            self._menu_1_li = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self._menu_1 = False
        elif tag == 'li':
            self._menu_1_li = False

    def handle_data(self, data):
        if self._menu_1_li:
            self._menu_1_list.append(data)



parser = MyHTMLParser()
parser.feed(html)

print(parser._menu_1_list)