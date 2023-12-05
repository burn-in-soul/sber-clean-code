from unittest import TestCase

from assets.asset import Asset
from market.market import Market
from portfolio.portfolio import Portfolio


class MarketTestCase(TestCase):

    def test_add(self):
        market = Market()
        asset = Asset(name='test')
        portfolio = Portfolio('Ivan')
        market.add(asset=asset, count=10, portfolio=portfolio)
        self.assertEqual(market._stock[0].asset, asset)
        self.assertEqual(market._stock[0].count, 10)
        self.assertEqual(market._stock[0].portfolio, portfolio)