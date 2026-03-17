from bank.currency import Currency


class Money:
    """
    Money is a Value Object that encapsulates an amount and a currency.
    This follows Object Calisthenics Rule 3: Wrap All Primitives And Strings.
    """

    def __init__(self, amount: float, currency: Currency) -> None:
        if not isinstance(currency, Currency):
            raise TypeError("Currency must be a Currency enum")
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.amount = amount
        self._currency = currency

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add Money with different currencies")
        return Money(self.amount + other.amount, self.currency)

    def times(self, multiplier: float) -> "Money":
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative")
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: float) -> "Money":
        if divisor <= 0:
            raise ValueError("Divisor must be greater than zero")
        return Money(self.amount / divisor, self.currency)

    @property
    def currency(self) -> Currency:
        return self._currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __repr__(self) -> str:
        return f"Money({self.amount}, {self._currency.value})"

    def __str__(self) -> str:
        return f"{self.amount} {self._currency.value}"
