from .exceptions import NotEnoughMoney


class Wallet:
    """Кошелек для хранения денег"""
    _amount: float = 0

    @property
    def amount(self) -> float:
        return self._amount

    def plus_amount(self, amount: float) -> None:
        self._amount += abs(amount)

    def minus_amount(self, amount: float) -> None:
        pos_amount = abs(amount)
        if self._amount >= pos_amount:
            self._amount -= pos_amount
        else:
            raise NotEnoughMoney(amount=pos_amount)
