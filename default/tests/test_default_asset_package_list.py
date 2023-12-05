from unittest import TestCase

from assets.asset import Asset
from assets.asset_package import AssetPackage
from assets.exceptions import AssetNotFound
from ..asset_package_list.default_asset_package_list import (
    DefaultAssetPackageList)


class DefaultAssetPackageListTestCase(TestCase):

    def setUp(self) -> None:
        self.first_asset = Asset('test')
        self.second_asset = Asset('test2')
        self.first_package = AssetPackage(asset=self.first_asset, count=10)
        self.second_package = AssetPackage(asset=self.second_asset, count=5)

    def test_find(self) -> None:
        package_list = DefaultAssetPackageList([self.first_package])
        result = package_list.find(self.first_asset)
        self.assertEqual(result, self.first_package)

    def test_find_not_found(self) -> None:
        package_list = DefaultAssetPackageList([self.first_package])
        with self.assertRaises(AssetNotFound):
            package_list.find(self.second_asset)
