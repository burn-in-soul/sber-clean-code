import abc
from abc import ABC
from typing import Type, TypeVar

from assets.asset import Asset
from ..asset_package.abc_asset_package import AssetPackageABC


class AssetPackageListABC(list, ABC):
    """Абстрактный список пакетов активов"""

    @abc.abstractmethod
    def find(self, asset: Asset) -> Type[AssetPackageABC]:
        pass

    @abc.abstractmethod
    def pick(self, asset: Asset, count: int) -> Type[AssetPackageABC]:
        pass

    @abc.abstractmethod
    def sum(self) -> float:
        pass


PackageList = TypeVar('PackageList', bound=AssetPackageListABC)
