from unittest import TestCase

from ..asset import Asset
from ..asset_package import AssetPackage
from ..asset_package_list import AssetPackageList
from ..exceptions import (AssetNotFound,
                          NotEnoughAssets)


class AssetPackageListTestCase(TestCase):

    def setUp(self) -> None:
        self.first_asset = Asset('test')
        self.second_asset = Asset('test2')
        self.first_package = AssetPackage(asset=self.first_asset, count=10)
        self.second_package = AssetPackage(asset=self.second_asset, count=5)

    def test_find(self) -> None:
        package_list = AssetPackageList([self.first_package])
        result = package_list.find(self.first_asset)
        self.assertEqual(result, self.first_package)

    def test_find_not_found(self) -> None:
        package_list = AssetPackageList([self.first_package])
        with self.assertRaises(AssetNotFound):
            package_list.find(self.second_asset)

    def test_append(self) -> None:
        package_list = AssetPackageList()
        package_list.append(self.first_package)
        self.assertEqual(package_list, [self.first_package])

    def test_append_already(self) -> None:
        package_list = AssetPackageList([self.first_package])
        third_package = AssetPackage(asset=self.first_asset, count=5)
        package_list.append(third_package)
        self.assertEqual(package_list, [self.first_package])
        self.assertEqual(package_list[0].count, 15)

    def test_pick_all(self) -> None:
        package_list = AssetPackageList([self.first_package])
        pick = package_list.pick(self.first_asset, 10)
        self.assertEqual(package_list, [])
        self.assertEqual(pick.asset, self.first_asset)
        self.assertEqual(pick.count, 10)

    def test_pick_part(self) -> None:
        package_list = AssetPackageList([self.first_package])
        pick = package_list.pick(self.first_asset, 2)
        self.assertEqual(package_list[0].asset, self.first_asset)
        self.assertEqual(package_list[0].count, 8)
        self.assertEqual(pick.asset, self.first_asset)
        self.assertEqual(pick.count, 2)

    def test_pick_not_found(self) -> None:
        package_list = AssetPackageList()
        with self.assertRaises(AssetNotFound):
            package_list.pick(self.first_asset, 2)

    def test_pick_extra(self) -> None:
        package_list = AssetPackageList([self.first_package])
        with self.assertRaises(NotEnoughAssets):
            package_list.pick(self.first_asset, 12)
