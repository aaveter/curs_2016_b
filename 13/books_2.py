

class Book:

    sum_pages_count = 0
    pages_count = 0
    author = 0
    title = None
    instances = []

    def __init__(self, author, pages_count, title):
        self.author = author
        self.pages_count = pages_count
        self.title = title

        Book.sum_pages_count += pages_count

        #self.instances = [self]

        self.instances.append(self) # пример работы с глобальным списком


    def print_info(self):
        print('''
        Название: {2}
        Автор:    {0}
        Страниц:  {1}
        Кол-во страниц в Библиотеке: {3}'''.format(
            self.author,
            self.pages_count,
            self.title,
            self.real_books_pages_count()
        )
        )

    # Создаем статический метод
    @staticmethod
    def real_books_pages_count(): # не привязан к объекту
        pages_count = 0
        for book in Book.instances:
            pages_count += book.pages_count
        return pages_count


book = Book('Чебурашка', 300, 'Успенский')
book2 = Book('Чебурашка 2', 300, 'Успенский')


print(Book.real_books_pages_count()) # Все нормально, метод класса

book2.print_info() # Ошибка, метод экземпляра