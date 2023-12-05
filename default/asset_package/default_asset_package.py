from assets.asset import Asset
from default.asset_package.abc_asset_package import AssetPackageABC
from market.default import prices


class DefaultAssetPackage(AssetPackageABC):
    """Пакет активов"""

    def __init__(self, asset: Asset, count: int) -> None:
        self.asset = asset
        self.count = count

    def __str__(self):
        return f'{self.asset}: {self.count}'

    @property
    def cost(self) -> float:
        return prices[self.asset] * self.count
