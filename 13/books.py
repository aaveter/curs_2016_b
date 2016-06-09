


class Book:

    sum_pages_count = 0
    pages_count = 0
    author = 0
    title = None

    def __init__(self, author, pages_count, title):
        self.author = author
        self.pages_count = pages_count
        self.title = title

        Book.sum_pages_count += pages_count
        #self.__class__.sum_pages_count += pages_count

    def print_info(self):
        print('''
        Название: {2}
        Автор:    {0}
        Страниц:  {1}'''.format(
            self.author,
            self.pages_count,
            self.title)
        )


voina_i_mir = Book('Лев Толстой', 3000, 'Война и мир')
evgeniy_onegin = Book('Александр Пушкин', 1000, 'Евгений Онегин')

# Основа основ
voina_i_mir.print_info()
evgeniy_onegin.print_info()

#print(dir(voina_i_mir))

print('pages_count:', Book.pages_count) # Глобальное значение

Book.pages_count = 100

print('pages_count:', Book.pages_count)

evgeniy_onegin.print_info()

Book('Чебурашка', 300, 'Успенский')

print( 'Всего страниц в Библиотеке:', Book.sum_pages_count )

