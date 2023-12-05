from typing import List

from assets.asset import Asset
from assets.exceptions import AssetNotFound, NotEnoughAssets
from default.asset_package.abc_asset_package import Package
from default.asset_package_list.default_asset_package_list import (
    DefaultAssetPackageList)
from .stock_asset_package import StockAssetPackage


class StockAssetPackageList(DefaultAssetPackageList):
    """Список пакетов активов"""

    def append(self, item: Package) -> None:
        super().append(item)

    def pick(self, asset: Asset, count: int) -> List[StockAssetPackage]:
        response = []
        try:
            package = self.find(asset)
        except AssetNotFound:
            raise NotEnoughAssets(count=count)
        else:
            if package.count == count:
                response.append(package)
                self.remove(package)
            elif package.count > count:
                new_package = StockAssetPackage(
                    asset=asset,
                    count=count,
                    portfolio=package.portfolio,
                )
                response.append(new_package)
                package.count -= count
            else:
                response.append(package)
                self.remove(package)
                response.extend(
                    self.pick(asset=asset, count=count - package.count),
                )
            return response
