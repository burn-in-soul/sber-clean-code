import abc
from abc import ABC
from typing import TypeVar

from assets.asset import Asset


class AssetPackageABC(ABC):
    """Пакет активов"""
    asset: Asset
    count: int

    @property
    @abc.abstractmethod
    def cost(self) -> float:
        pass


Package = TypeVar('Package', bound=AssetPackageABC)
