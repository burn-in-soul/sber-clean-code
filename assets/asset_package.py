from default.asset_package.default_asset_package import DefaultAssetPackage
from .asset import Asset
from .exceptions import CreateZeroPackage


class AssetPackage(DefaultAssetPackage):
    """Пакет активов"""
    asset: Asset
    count: int

    def __init__(self, asset: Asset, count: int) -> None:
        if count != 0:
            super().__init__(asset, count)
        else:
            raise CreateZeroPackage()
