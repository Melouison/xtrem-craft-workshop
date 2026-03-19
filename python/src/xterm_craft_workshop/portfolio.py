from xterm_craft_workshop.bank import Bank

from .money import Money


class Portfolio:
    def __init__(self, pivot):
        self.monies = []
        self.bank = Bank(pivot)

    def reset(self,pivot):
        self.monies = []
        self.bank = Bank(pivot)


    def add(self, money):
        self.monies.append(money)

    def evaluate(self, target_currency):
        total = 0
        for money in self.monies:
            total += self.bank.convert_money(money, target_currency)
        return total
