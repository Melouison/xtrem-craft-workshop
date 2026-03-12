import pytest
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator
from xterm_craft_workshop.money import Money

class TestMoney:
    def test_add_in_usd_returns_value(self):
        five_dollars = Money(5, Currency.USD)
        ten_dollars = Money(10, Currency.USD)
        ten_euros = Money(10, Currency.EUR)
        with pytest.raises(ValueError):
            five_dollars.add(ten_euros) 
        assert five_dollars.add(ten_dollars) == Money(15, Currency.USD)
        
    def test_multiply_in_euros_returns_positive_number(self,):
        ten_euros = Money(10, Currency.EUR)       
        assert ten_euros.times(2) == Money(20, Currency.EUR)
        with pytest.raises(ValueError):
            ten_euros.times(-1)
        # a changer peut etre apres 

    def test_divide_in_korean_won_returns_float(self):
        one_hundred_euros = Money(100, Currency.EUR)
        assert one_hundred_euros.divide(4) == Money(25, Currency.EUR)
        with pytest.raises(ValueError):
            one_hundred_euros.divide(0)
            one_hundred_euros.divide(-10)
    
    def test_equal (self):
        assert Money(10, Currency.USD) == Money(10, Currency.USD)
        assert Money(10, Currency.USD) != Money(10, Currency.EUR)
        
    def test_money_superieur_a_zero(self):
        with pytest.raises(ValueError):
            Money(-1, Currency.USD)
        Money(0, Currency.USD)
        Money(10, Currency.USD)
