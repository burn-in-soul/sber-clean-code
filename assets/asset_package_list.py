from default.asset_package.abc_asset_package import Package
from default.asset_package_list.default_asset_package_list import (
    DefaultAssetPackageList)
from .asset import Asset
from .asset_package import AssetPackage
from .exceptions import AssetNotFound, NotEnoughAssets, CreateZeroPackage


class AssetPackageList(DefaultAssetPackageList):
    """Список пакетов активов"""

    def append(self, item: Package) -> None:
        try:
            already_in = self.find(item.asset)
        except AssetNotFound:
            super().append(item)
        else:
            already_in.count += item.count

    # atomic
    def pick(self, asset: Asset, count: int) -> Package:
        package = self.find(asset)
        if package.count < count:
            raise NotEnoughAssets(count)
        else:
            self.remove(package)
            picking = AssetPackage(package.asset, count=count)
            try:
                saving = AssetPackage(package.asset,
                                      count=package.count - count)
            except CreateZeroPackage:
                pass
            else:
                self.append(saving)
            return picking
