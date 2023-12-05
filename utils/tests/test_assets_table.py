from unittest import TestCase

from market.asset_price import VK_ASSET, YANDEX_ASSET, SBER_ASSET
from market.stock_asset_package import StockAssetPackage
from market.stock_asset_package_list import StockAssetPackageList
from portfolio.portfolio import Portfolio
from utils.assets_table import AssetsTable


class AssetsTableTestCase(TestCase):

    def setUp(self) -> None:
        portfolio = Portfolio('Vasya')
        first = StockAssetPackage(asset=VK_ASSET, count=5,
                                  portfolio=portfolio)
        second = StockAssetPackage(asset=YANDEX_ASSET, count=12,
                                   portfolio=portfolio)
        third = StockAssetPackage(asset=SBER_ASSET, count=10,
                                  portfolio=portfolio)
        self.stock = StockAssetPackageList([first, second, third])

    def test_create(self):
        table = ('| Актив   |   Цена |   Количество |\n'
                 '|---------+--------+--------------|\n'
                 '| vk      |  502.4 |            5 |\n'
                 '| yandex  | 1000   |           12 |\n'
                 '| sber    |  100.4 |           10 |')
        self.assertEqual(table, AssetsTable(self.stock).create())
