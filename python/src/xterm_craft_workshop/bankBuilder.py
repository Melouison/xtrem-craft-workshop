from typing import Dict

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency


class bankBuilder:


    def __init__(self):
        self._exchange_rate: Dict[str, float] = {}
        self.pivot = Currency.EUR

    @staticmethod
    def a_bankbuilder():
        return bankBuilder()

    def with_exchange_rate(self, currency : Currency, rate : float ):
        if (rate <= 0):
            raise ValueError("Rate must be positive")
        key = f"{self.pivot.value}->{currency.value}"
        self._exchange_rate[key] = rate
        return self

    def with_not_money_pivot(self):
        self.pivot = None
        return self

    def with_money_pivot(self, currency : Currency):
        self.pivot = currency
        return self

    def with_exchange_rates(self, rates : Dict[str, float]):
        self._exchange_rate = rates
        return self

    def build(self) -> Bank:
        return Bank(self.pivot, self._exchange_rate) 