






html = '''<html>
<body>
    <form>
        <input name='name' type='text' value='Alex'>
        <input name='password' type='password' value='vfe8nhdn'>
        <input type='submit'>
    </form>
</body>
</html>'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    _span = False
    _names = []

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            print(attrs)
            for name, value in attrs:
                if name == 'class' and value == cls:
                    self._span = True

    def handle_endtag(self, tag):
        if tag == 'span':
            self._span = False

    def handle_data(self, data):
        if self._span:
            self._names.append(data)