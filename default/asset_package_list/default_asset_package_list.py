import abc
from typing import List

from assets.asset import Asset
from assets.exceptions import AssetNotFound
from .abc_asset_package_list import AssetPackageListABC
from ..asset_package.abc_asset_package import Package


class DefaultAssetPackageList(AssetPackageListABC):
    """Список пакетов активов"""

    def __init__(self, deals: List[Package] = None) -> None:
        super().__init__(deals or [])

    def __setitem__(self, index, item: Package) -> None:
        super().__setitem__(index, item)

    def __str__(self) -> str:
        return ', '.join(map(str, self))

    @abc.abstractmethod
    def append(self, item: Package) -> None:
        super().append(item)

    def find(self, asset: Asset) -> Package:
        try:
            package = next(package for package in self if
                           package.asset == asset)
        except StopIteration:
            raise AssetNotFound(asset=asset)
        else:
            return package

    @abc.abstractmethod
    def pick(self, asset: Asset, count: int) -> Package:
        pass

    def sum(self) -> float:
        return sum(package.cost for package in self)
