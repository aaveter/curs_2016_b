
# ООП в Python

def func():
    pass

print( func )


x = 10
s = 'Строка'
func.some_attribute = 112



# Классы и Объекты

class A: # Обозначаем класс А
    pass

a = A()

print( a )


class A: # Обозначаем класс А
    pass

print(a.name, a.age)  # Ошибка, нет аттрибутов


# Функциональность

class Student:

    # Глобальные переменные класса
    # = значения по умолчанию для всех экземпляров
    # = впринципе общие атрибуты для экземпляров

    name = 'Без имени'
    age = 0


stud1 = Student()
stud1.name = 'Мария'
#stud1.age = 17
print(stud1.name, stud1.age)


class Student:
    name = 'Без имени'
    age = 0

    def some_method(self): # Обязательно self
        # по self экземляр
        print(self.name, self.age)


stud2 = Student()
stud2.some_method()




class Student:
    print('Student')

    name = 'Без имени'
    age = 0

    # конструктор
    def __init__(self, name, age, *args, **kwargs):
        # Логика создания экземпляра
        print('конструтор')
        self.name = name
        self.age = age

    def some_method(self, privetstvie=''):  # Обязательно self
        # по self экземляр
        print('some_method')
        print(privetstvie, self.name, self.age)


stud3 = Student(name='Григорий', age=14)
stud3.some_method(privetstvie='Это студент:')





class Book:

    pages_count = 0
    author = 0
    title = None

    def __init__(self, author, pages_count, title):
        self.author = author
        self.pages_count = pages_count
        self.title = title

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
evgeniy_onegin = Book('Александр Пушкин', 3000, 'Евгений Онегин')

# Основа основ
voina_i_mir.print_info()
evgeniy_onegin.print_info()

print(dir(voina_i_mir))