from assets.asset import Asset
from default.asset_package.default_asset_package import DefaultAssetPackage
from portfolio.portfolio import Portfolio


class StockAssetPackage(DefaultAssetPackage):
    """Пакет активов на бирже"""

    def __init__(self, asset: Asset, count: int, portfolio: Portfolio) -> None:
        super().__init__(asset, count)
        self.portfolio = portfolio
