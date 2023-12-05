from unittest import TestCase

from assets.asset import Asset
from market.asset_price import AssetPrice, YANDEX_ASSET


class AssetPriceTestCase(TestCase):

    def test_add(self):
        price = AssetPrice()
        new_asset = Asset(name='Linkedin')
        price[new_asset] = 100
        self.assertEqual(price[new_asset], 100)

    def test_update(self):
        price = AssetPrice()
        price[YANDEX_ASSET] = 100
        self.assertEqual(price[YANDEX_ASSET], 100)
