

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
        Кол-во книг в Библиотеке: {3}'''.format(
            self.author,
            self.pages_count,
            self.title,
            len(self.instances)
        )
        )

    def real_books_pages_count(self):
        pages_count = 0
        for book in Book.instances:
            pages_count += book.pages_count
        return pages_count



Book('Лев Толстой', 3000, 'Война и мир')
Book('Александр Пушкин', 1000, 'Евгений Онегин')
cheburashka = Book('Чебурашка', 300, 'Успенский')

cheburashka.pages_count = 500 # изменилось кол-во страниц


print( 'Всего страниц в Библиотеке:', cheburashka.real_books_pages_count() )

# for book in Book.instances:
#     book.print_info()