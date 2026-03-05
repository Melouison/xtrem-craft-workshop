from typing import Dict
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(currency1: Currency, currency2: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.add_echange_rate(currency1, currency2, rate)

        return bank

    def add_echange_rate(self, c1: Currency, c2: Currency, rate: float) -> None:

        self._exchange_rate[f"{c1.value}->{c2.value}"] = rate

    def convert(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, cur_target)

