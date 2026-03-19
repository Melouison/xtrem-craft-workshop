from typing import Dict

from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self,  pivot : Currency, exchange_rate = {} ) -> None:
        if pivot not in [Currency.EUR, Currency.USD, Currency.KRW]:
            raise ValueError("Pivot currency must be EUR, USD or KRW")
        self._exchange_rate = exchange_rate
        self.pivot = pivot
        self._exchange_rate[f"{pivot.value}->{pivot.value}"] = 1.0

    @staticmethod
    def create(currency: Currency, rate: float, pivot: Currency) -> "Bank":
        bank = Bank(pivot, {})
        bank.add_echange_rate( currency, rate)

        return bank

    def add_echange_rate(self, c2: Currency, rate: float) -> None:

        self._exchange_rate[f"{self.pivot.value}->{c2.value}"] = rate

    def convert(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return round(amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"], 2)
        if f"{cur_target.value}->{cur_origin.value}" in self._exchange_rate :
           return round(amount / self._exchange_rate[f"{cur_target.value}->{cur_origin.value}"], 2)
        if cur_origin.value == cur_target.value:
            return amount
        if f"{self.pivot.value}->{cur_origin.value}" in self._exchange_rate and f"{self.pivot.value}->{cur_target.value}" in self._exchange_rate:
            amount_in_pivot = amount / self._exchange_rate[f"{self.pivot.value}->{cur_origin.value}"]
            return round(amount_in_pivot * self._exchange_rate[f"{self.pivot.value}->{cur_target.value}"], 2)

        raise MissingExchangeRateError(cur_origin, cur_target)

    def convert_money(self, money, target_currency):
        if f"{money.currency.value}->{target_currency.value}" in self._exchange_rate:
            return round(money.amount * self._exchange_rate[f"{money.currency.value}->{target_currency.value}"], 2)
        if money.currency.value == target_currency.value:
            return money.amount
        if f"{self.pivot.value}->{money.currency.value}" in self._exchange_rate and f"{self.pivot.value}->{target_currency.value}" in self._exchange_rate:
            amount_in_pivot = money.amount / self._exchange_rate[f"{self.pivot.value}->{money.currency.value}"]
            return round(amount_in_pivot * self._exchange_rate[f"{self.pivot.value}->{target_currency.value}"], 2)
        raise MissingExchangeRateError(money.currency, target_currency)
