

# шаблон "Наблюдатель"

from random import choice










# Избиратель
class Choicer:

    # кладет бюллетень
    def choice(self, variants):
        self.my_choice = choice(variants)
        return self.my_choice

    # Реакция на итоги выборов
    def react(self, prezident):
        if prezident == self.my_choice:
            print('URAAAAAA!!!! =))))')
        else:
            print('.. sad ...(')













# Избирательный участок (субъект)
class ChoiceBox:

    def __init__(self, variants):
        # список участников голования
        self.variants = variants

    def vibori(self, choicers):
        self.choicers = choicers

        results = {}

        # сам процесс выборов в течение дня
        for choicer in choicers:
            choice = choicer.choice(self.variants)
            if choice in results:
                results[choice] += 1
            else:
                results[choice] = 1

        # подведение итогов
        lst = [a for a in sorted(results, key=lambda i: results[i])]
        prezident = lst[-1]
        print(prezident)

        # оповещаем страну
        for choicer in choicers:
            choicer.react(prezident)


uchastok = ChoiceBox(variants=['Кирилл', 'Петр', 'Олег'])
uchastok.vibori([Choicer() for a in range(20)])