from unittest import TestCase

from ..asset import Asset
from ..asset_package import AssetPackage
from ..exceptions import CreateZeroPackage


class AssetPackageTestCase(TestCase):

    def test_zero_init(self) -> None:
        asset = Asset(name='test')
        with self.assertRaises(CreateZeroPackage):
            AssetPackage(asset=asset, count=0)
