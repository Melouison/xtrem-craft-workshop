import pytest
import re

from bank.bank import Bank
from bank.currency import Currency
from bank.missing_exchange_rate_error import MissingExchangeRateError


class TestBank:
    def test_should_return_float_when_convertng_euro_to_usd(self):
        assert Bank.create(Currency.EUR, Currency.USD, 1.2).convert(10, Currency.EUR, Currency.USD) == 12

    def test_should_return_same_value_when_converting_currency_to_itself(self):
        assert Bank.create(Currency.EUR, Currency.USD, 1.2).convert(10, Currency.EUR, Currency.EUR) == 10

    def test_should_not_convert_between_different_currencies_when_exchange_rate_is_missing(self):
        with pytest.raises(MissingExchangeRateError) as error:
            Bank.create(Currency.EUR, Currency.USD, 1.2).convert(10, Currency.EUR, Currency.KRW)
        assert str(error.value) == "EUR->KRW"

    def test_should_returns_differents_floats_whenconverintngf_different_exchange_rate(self):
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert bank.convert(10, Currency.EUR, Currency.USD) == 12

        bank.add_echange_rate(Currency.EUR, Currency.USD, 1.3)
        assert bank.convert(10, Currency.EUR, Currency.USD) == 13

