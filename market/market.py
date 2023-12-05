from typing import List

from assets.asset import Asset
from portfolio.portfolio import Portfolio
from utils.assets_table import AssetsTable
from .default import prices
from .stock_asset_package import StockAssetPackage
from .stock_asset_package_list import StockAssetPackageList


class Market:
    _stock: StockAssetPackageList = StockAssetPackageList()

    def add(self, asset: Asset, count: int, portfolio: Portfolio) -> None:
        new_package = StockAssetPackage(
            asset=asset,
            count=count,
            portfolio=portfolio,
        )
        self._stock.append(new_package)

    def pick(self, asset: Asset, count) -> List[StockAssetPackage]:
        return self._stock.pick(asset, count)

    def show_stock(self) -> None:
        print(AssetsTable(self._stock).create())

    @staticmethod
    def find_price(asset: Asset) -> float:
        return prices[asset]
