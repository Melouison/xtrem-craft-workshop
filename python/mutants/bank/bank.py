from typing import Dict
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        args = [exchange_rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁBankǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁBankǁ__init____mutmut_orig(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    def xǁBankǁ__init____mutmut_1(self, exchange_rate = {}) -> None:
        self._exchange_rate = None
    
    xǁBankǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁ__init____mutmut_1': xǁBankǁ__init____mutmut_1
    }
    xǁBankǁ__init____mutmut_orig.__name__ = 'xǁBankǁ__init__'

    @staticmethod
    def create(currency1: Currency, currency2: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.add_echange_rate(currency1, currency2, rate)

        return bank

    def add_echange_rate(self, c1: Currency, c2: Currency, rate: float) -> None:
        args = [c1, c2, rate]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁadd_echange_rate__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁadd_echange_rate__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁadd_echange_rate__mutmut_orig(self, c1: Currency, c2: Currency, rate: float) -> None:

        self._exchange_rate[f"{c1.value}->{c2.value}"] = rate

    def xǁBankǁadd_echange_rate__mutmut_1(self, c1: Currency, c2: Currency, rate: float) -> None:

        self._exchange_rate[f"{c1.value}->{c2.value}"] = None
    
    xǁBankǁadd_echange_rate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁadd_echange_rate__mutmut_1': xǁBankǁadd_echange_rate__mutmut_1
    }
    xǁBankǁadd_echange_rate__mutmut_orig.__name__ = 'xǁBankǁadd_echange_rate'

    def convert(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        args = [amount, cur_origin, cur_target]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁBankǁconvert__mutmut_orig'), object.__getattribute__(self, 'xǁBankǁconvert__mutmut_mutants'), args, kwargs, self)

    def xǁBankǁconvert__mutmut_orig(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, cur_target)

    def xǁBankǁconvert__mutmut_1(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" not in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, cur_target)

    def xǁBankǁconvert__mutmut_2(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount / self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, cur_target)

    def xǁBankǁconvert__mutmut_3(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value != cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, cur_target)

    def xǁBankǁconvert__mutmut_4(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(None, cur_target)

    def xǁBankǁconvert__mutmut_5(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, None)

    def xǁBankǁconvert__mutmut_6(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_target)

    def xǁBankǁconvert__mutmut_7(self, amount: float, cur_origin: Currency, cur_target: Currency) -> float:
        if f"{cur_origin.value}->{cur_target.value}" in self._exchange_rate:
           return amount * self._exchange_rate[f"{cur_origin.value}->{cur_target.value}"]
        if cur_origin.value == cur_target.value:
            return amount
        raise MissingExchangeRateError(cur_origin, )
    
    xǁBankǁconvert__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁBankǁconvert__mutmut_1': xǁBankǁconvert__mutmut_1, 
        'xǁBankǁconvert__mutmut_2': xǁBankǁconvert__mutmut_2, 
        'xǁBankǁconvert__mutmut_3': xǁBankǁconvert__mutmut_3, 
        'xǁBankǁconvert__mutmut_4': xǁBankǁconvert__mutmut_4, 
        'xǁBankǁconvert__mutmut_5': xǁBankǁconvert__mutmut_5, 
        'xǁBankǁconvert__mutmut_6': xǁBankǁconvert__mutmut_6, 
        'xǁBankǁconvert__mutmut_7': xǁBankǁconvert__mutmut_7
    }
    xǁBankǁconvert__mutmut_orig.__name__ = 'xǁBankǁconvert'

