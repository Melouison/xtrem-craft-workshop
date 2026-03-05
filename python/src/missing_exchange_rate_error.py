from .currency import Currency


class MissingExchangeRateError(Exception):
    def __init__(self, c1: Currency, c2: Currency) -> None:
        super().__init__(f"{c1.value}->{c2.value}")
