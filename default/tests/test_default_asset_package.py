from unittest import TestCase

from assets.asset import Asset
from ..asset_package.default_asset_package import DefaultAssetPackage


class DefaultAssetPackageTestCase(TestCase):

    def test_cost(self) -> None:
        asset = Asset(name='yandex')
        package = DefaultAssetPackage(asset=asset, count=10)
        self.assertEqual(package.cost, 10000.0)
