import pytest
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.bankBuilder import bankBuilder

class TestBank:
    """une bank avec EURO en pivot EUR et sans pivot ce qui provoque une erreur"""
    def test_bankbuilder(self):
        bank = (bankBuilder.a_bankbuilder()
                .with_currency_pivot(Currency.EUR)
                    .with_exchange_rate(Currency.USD, 1.2)
                            .build())

        money = Money(10, Currency.EUR)
        result = bank.convert_money(money, Currency.USD)
        assert result == 12

        with pytest.raises(ValueError):
             bank2 = (bankBuilder.a_bankbuilder()
                .with_exchange_rate(Currency.USD, 1.2)
                .with_not_currency_pivot()
                .build()
            )




    def test_same_currency(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.EUR)
                            .with_exchange_rate( Currency.USD, 1.2)
                            .build())

        money = Money(10, Currency.EUR)
        result = bank.convert_money(money, Currency.EUR)
        assert result == 10

    def test_missing_exchange_rate(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.EUR)
                            .with_exchange_rate(Currency.USD, 1.2)
                            .build())

        money = Money(10, Currency.EUR)
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert_money(money, Currency.KRW)
        assert str(error.value) == "EUR->KRW"

    def test_different_exchange_rate(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.EUR)
                            .with_exchange_rate(Currency.USD, 1.2)
                            .build())
        
        money = Money(10, Currency.EUR)
        result = bank.convert_money(money, Currency.USD)
        assert result == 12

        bank = bankBuilder.a_bankbuilder().with_currency_pivot(Currency.EUR).with_exchange_rate(Currency.USD, 1.3).build()
        money = Money(10, Currency.EUR)
        result = bank.convert_money(money, Currency.USD)
        assert result == 13

    
    def test_converter_money(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.EUR)
                            .with_exchange_rate(Currency.USD, 1.2)
                            .build())
        money = Money(10, Currency.EUR)
        result = bank.convert_money(money, Currency.USD)
        assert result == 12

    """"Etant donné une banque avec devise pivot
    Lorsque je veux ajouter un exhcange rate
    Alors le calcule d'échange devra utilisé ce pivot dans les 2 sens """
    def test_convert_non_pivot(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.EUR)
                            .with_exchange_rate(Currency.USD, 0.9)
                            .build())
        money = Money(100, Currency.USD)
        result = bank.convert_money(money,Currency.EUR)
        assert result == 111.11

    """ Etant donné une banque avec l'EUR comme devise pivot et un taux de change en USD de 1.2,
    Lorsque je veux convertir 10 EUR en USD,
    Alors la banque me renvoie 12 USD """
    def test_convert_pivot(self):
        bank = (bankBuilder.a_bankbuilder()
                            .with_currency_pivot(Currency.USD)
                            .with_exchange_rate(Currency.EUR, 0.9)
                            .build())
        money = Money(100, Currency.USD)
        result = bank.convert_money(money,Currency.EUR)
        assert result == 90

    """ Test avec taux de change négatif """
    def test_convert_exchange_rate_negative(self):
        with pytest.raises(ValueError):
            bank = (bankBuilder.a_bankbuilder()
                        .with_currency_pivot(Currency.USD)
                        .with_exchange_rate(Currency.EUR, -0.9)
                        .build())
    