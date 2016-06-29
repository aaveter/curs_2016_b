

# Шаблоны проектирования (Templates)



class Calculator:

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

calc = Calculator()
print( calc.plus(10, 20) )
print( calc.minus(10, 20) )


# -----------------------
# "Команда"

class Action:

    def execute(self, a, b):
        pass

class Plus(Action):

    def execute(self, a, b):
        return a + b

class SmartPlus(Plus):

    def execute(self, a, b):
        return int(float(a) + float(b))

class Minus(Action):

    def execute(self, a, b):
        return a - b

# ...


class Calculator:

    operations = {
        '+': SmartPlus(),
        '-': Minus(),
        #...
    }

    def execute(self, operation, a, b):
        op = self.operations.get(operation)
        return op.execute(a, b)


calc = Calculator()
print( calc.execute('+', 20, 30) )
print( calc.execute('-', 20, 30) )


# -------------------------
# или Более коротки вариант:

class Calculator:

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        #...
    }

    def execute(self, operation, a, b):
        op = self.operations.get(operation)
        return op(a, b)

calc = Calculator()
print( calc.execute('+', 20, 30) )
print( calc.execute('-', 20, 30) )