class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'num one  is: {self.num1}\n' \
               f'num two  is: {self.num2}\n' \

    def __add__(self):

        return print(f'{self.num1} + {self.num2} = {self.num1 + self.num2}')

    def __sub__(self):
        return print(f'{self.num1} - {self.num2} = {self.num1 - self.num2}')

    def __mul__(self):
        return print(f'{self.num1} * {self.num2} = {self.num1 * self.num2}')

    def __truediv__(self):
        return print(f'{self.num1} / {self.num2} = {self.num1 / self.num2}')


c = Calculator(25, 10)
print(c)
c.__add__()
c.__sub__()
c.__mul__()
c.__truediv__()