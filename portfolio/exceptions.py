class NotEnoughMoney(Exception):

    def __init__(self, amount: float):
        self._amount = amount

    def __str__(self) -> str:
        return f'There are less than {self._amount} money in wallet'
