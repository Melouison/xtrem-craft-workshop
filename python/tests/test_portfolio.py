import pytest
from bank.currency import Currency
from .portfolio import portfolio

class TestPortfolio:
    portfolioe = portfolio()
        
    def test_addition_for_empty_portfolio(self):
        self.portfolioe.reset()
        self.portfolioe.add (12, Currency.EUR)
        assert self.portfolioe.evaluate(Currency.EUR) == 12
    
    def test_change_rate_conversion(self):
        self.portfolioe.reset()
        self.portfolioe.add (12, Currency.EUR)
        self.portfolioe.bank.add_echange_rate(Currency.EUR, Currency.USD, 1.2)
        assert self.portfolioe.evaluate(Currency.USD) == pytest.approx(14.4)
        
    def test_portfolio_several_currencies(self):
        self.portfolioe.reset()
        self.portfolioe.add (10, Currency.EUR)
        self.portfolioe.add (5, Currency.EUR)
        assert self.portfolioe.evaluate(Currency.EUR) == 15

    def test_portfolio_return_empty_when_empty_no_fucking_way(self):
        self.portfolioe.reset()
        assert self.portfolioe.evaluate(Currency.USD) == 0

    def test_portfolio_evaluation_differents_currencies(self):
        self.portfolioe.reset()
        self.portfolioe.add (10, Currency.EUR)
        self.portfolioe.add (5, Currency.USD)
        self.portfolioe.bank.add_echange_rate(Currency.EUR, Currency.USD, 1.2)
        self.portfolioe.bank.add_echange_rate(Currency.USD, Currency.EUR, 0.83)
        assert self.portfolioe.evaluate(Currency.EUR) == pytest.approx(14.15)
        assert self.portfolioe.evaluate(Currency.USD) == pytest.approx(17)


    def test_amounts_must_be_converted_into_the_target_currency_before_addition(self):
        self.portfolioe.reset()
        self.portfolioe.add (10, Currency.EUR)
        self.portfolioe.add (5, Currency.USD)
        self.portfolioe.bank.add_echange_rate(Currency.USD, Currency.EUR, 0.83)
        assert self.portfolioe.evaluate(Currency.EUR) == pytest.approx(14.15)
