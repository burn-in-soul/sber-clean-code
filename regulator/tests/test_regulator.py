from unittest import TestCase

from assets.asset import Asset
from assets.asset_package import AssetPackage
from market.asset_price import YANDEX_ASSET, SBER_ASSET
from market.market import Market
from portfolio.portfolio import Portfolio
from regulator.regulator import Regulator


class RegulatorTestCase(TestCase):

    def setUp(self) -> None:
        self.market = Market()
        self.vasya = Portfolio(name='Вася')
        self.vasya.wallet.plus_amount(5000)
        self.sasha = Portfolio(name='Саша')
        self.sasha.wallet.plus_amount(1000)
        self.first_asset = YANDEX_ASSET
        self.second_asset = SBER_ASSET
        first_package = AssetPackage(asset=self.first_asset, count=20)
        self.sasha.append(first_package)
        second_package = AssetPackage(asset=self.second_asset, count=5)
        self.vasya.append(second_package)
        self.regulator = Regulator(market=self.market)

    def test_money_transfer(self):
        self.regulator._money_transfer(self.vasya, self.sasha, 500)
        self.assertEqual(self.vasya.wallet.amount, 5500)
        self.assertEqual(self.sasha.wallet.amount, 500)

    def test_from_portfolio_to_market(self):
        self.regulator.from_portfolio_to_market(self.vasya, self.second_asset,
                                                5)
        self.assertEqual(len(self.vasya._assets), 0)
        self.assertEqual(len(self.market._stock), 1)
        self.assertEqual(self.market._stock[0].asset, self.second_asset)
        self.assertEqual(self.market._stock[0].count, 5)
        self.assertEqual(self.market._stock[0].portfolio, self.vasya)

    def test_from_market_to_portfolio(self):
        self.regulator.from_portfolio_to_market(self.vasya, self.second_asset,
                                                5)
        self.regulator.from_market_to_portfolio(self.sasha, self.second_asset,
                                                5)
        self.assertEqual(len(self.vasya._assets), 0)
        self.assertEqual(len(self.market._stock), 0)
        self.assertEqual(len(self.sasha._assets), 2)
        self.assertEqual(self.sasha._assets[1].asset, self.second_asset)
        self.assertEqual(self.sasha._assets[1].count, 5)
        self.assertEqual(self.sasha.wallet.amount, 498.0)
