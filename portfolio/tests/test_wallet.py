from unittest import TestCase

from ..exceptions import NotEnoughMoney
from ..wallet import Wallet


class WalletTestCase(TestCase):

    def test_get_amount(self) -> None:
        wallet = Wallet()
        self.assertEqual(wallet.amount, 0)

    def test_change_amount(self) -> None:
        wallet = Wallet()
        wallet.plus_amount(10)
        self.assertEqual(wallet.amount, 10)

    def test_change_amount_munis(self) -> None:
        wallet = Wallet()
        wallet._amount = 10
        wallet.minus_amount(8)
        self.assertEqual(wallet.amount, 2)

    def test_change_amount_munis_exception(self) -> None:
        wallet = Wallet()
        with self.assertRaises(NotEnoughMoney):
            wallet.minus_amount(8)
