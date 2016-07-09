


cls = 'snippet-card__header-text'

html = open('search?cvredirect=2').read()

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


parser = MyHTMLParser()
parser.feed(html)

print(parser._names)