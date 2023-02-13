class Bank:
    def __init__(self, _name, _balanse):
        self._name = _name
        self._balanse = _balanse

    def __str__(self):
        return f' name is: {self._name}\n' \
               f'balanse is: {self._balanse}'

    def moneyX(self):
        balanse = int(input("Введите сумму: "))
        self._balanse += balanse

    def _kill(self):
        self._balanse *= 0

    def kill(self):
        self._kill()

    def __jackpot(self):
        self._balanse *= 10

    def jackpot(self):
        self.__jackpot()

    def _balanse_stealer(self, other):
        self._balanse += other._balanse


name1 = Bank("name1", 250)
name2 = Bank("name2", 250)
name3 = Bank("name3", 250)
name4 = Bank("name4", 250)
name5 = Bank("name5", 250)

name1.moneyX()
print(name1)

name2.kill()
print(name2)

name3.jackpot()

print(name3)

name4._balanse_stealer(name5)
print(name4)
