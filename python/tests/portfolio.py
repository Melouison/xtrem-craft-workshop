from bank.bank import Bank


class portfolio:
    def __init__(self):
        self.currencies = []
        self.bank = Bank()

    def reset(self):
        self.currencies = []

    def add(self, amount, currency):
        self.currencies.append((amount, currency))

    def evaluate(self, target_currency):
        total = 0
        for amount, currency in self.currencies:
            if currency == target_currency:
                total += amount
            else:
                total += self.convert(amount, currency, target_currency)
        return total

    def convert(self, amount, from_currency, to_currency):

        return self.bank.convert(amount, from_currency, to_currency)