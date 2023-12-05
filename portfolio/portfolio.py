from assets.asset_package import AssetPackage
from assets.asset_package_list import AssetPackageList
from assets.asset import Asset
from .wallet import Wallet


class Portfolio:
    """Портфель"""
    _assets: AssetPackageList
    wallet: Wallet

    def __init__(self, name: str) -> None:
        self.name = name
        self._assets = AssetPackageList()
        self.wallet = Wallet()

    def __str__(self) -> str:
        return self.name

    @property
    def current_cost(self) -> float:
        return self._assets.sum()

    def pick(self, asset: Asset, count: int) -> None:
        package = self._assets.pick(asset=asset, count=count)

    # atomic
    def append(self, asset_package: AssetPackage) -> None:
        self._assets.append(asset_package)
