
students = [
    ['Mark', 23, 5],
    ['Olga', 23, 4],
]

# def vivod(name, old, mark):
#     print('Имя:', name, 'Возраст:', old, 'Оценка:', mark)


def students_vivod(students):
    for student in students:
        # name = student[0]
        # old = student[1]
        # mark = student[2]

        vivod(student[0], student[1], student[2])


def vivod(name, old, mark):
     print('Имя:', name, 'Возраст:', old, 'Оценка:', mark)


students_vivod(students)