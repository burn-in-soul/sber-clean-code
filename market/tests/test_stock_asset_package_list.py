from unittest import TestCase

from assets.asset import Asset
from assets.exceptions import NotEnoughAssets
from portfolio.portfolio import Portfolio
from ..stock_asset_package import StockAssetPackage
from ..stock_asset_package_list import StockAssetPackageList


class StockAssetPackageListTestCase(TestCase):

    def setUp(self) -> None:
        self.first_asset = Asset(name='test')
        self.second_asset = Asset(name='test2')
        portfolio = Portfolio(name='Vitya')
        self.first_package = StockAssetPackage(asset=self.first_asset,
                                               count=10,
                                               portfolio=portfolio)
        self.second_package = StockAssetPackage(asset=self.second_asset,
                                                count=5,
                                                portfolio=portfolio)
        self.third_package = StockAssetPackage(asset=self.second_asset,
                                               count=10,
                                               portfolio=portfolio)

    def test_append(self):
        package_list = StockAssetPackageList()
        package_list.append(self.first_package)
        self.assertEqual(package_list[0], self.first_package)

    def test_pick_one(self):
        package_list = StockAssetPackageList()
        package_list.append(self.first_package)
        package_list.append(self.second_package)
        picked = package_list.pick(asset=self.first_asset, count=10)
        self.assertEqual(picked[0].asset, self.first_asset)
        self.assertEqual(picked[0].count, 10)
        self.assertEqual(package_list[0].asset, self.second_asset)
        self.assertEqual(package_list[0].count, 5)
        self.assertEqual(len(package_list), 1)

    def test_pick_from_two(self):
        package_list = StockAssetPackageList()
        package_list.append(self.first_package)
        package_list.append(self.second_package)
        package_list.append(self.third_package)
        picked = package_list.pick(asset=self.second_asset, count=15)
        self.assertEqual(picked[0].asset, self.second_asset)
        self.assertEqual(picked[0].count, 5)
        self.assertEqual(picked[1].asset, self.second_asset)
        self.assertEqual(picked[1].count, 10)
        self.assertEqual(package_list[0].asset, self.first_asset)
        self.assertEqual(package_list[0].count, 10)
        self.assertEqual(len(package_list), 1)

    def test_pick_not_enough(self):
        package_list = StockAssetPackageList()
        package_list.append(self.first_package)
        package_list.append(self.second_package)
        package_list.append(self.third_package)
        with self.assertRaises(NotEnoughAssets):
            picked = package_list.pick(asset=self.second_asset, count=20)
            print(picked)
