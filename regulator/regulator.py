from assets.asset import Asset
from assets.asset_package import AssetPackage
from market.market import Market
from portfolio.portfolio import Portfolio


class Regulator:
    """Регулятор. Проводит сделки на бирже"""

    def __init__(self, market: Market) -> None:
        self._market = market

    # Методы должны быть атомарными
    def from_portfolio_to_market(self, portfolio: Portfolio,
                                 asset: Asset, count: int) -> None:
        portfolio.pick(asset, count)
        self._market.add(asset, count, portfolio)

    def from_market_to_portfolio(self, portfolio: Portfolio,
                                 asset: Asset, count: int) -> None:
        picked_packages = self._market.pick(asset, count)
        for package in picked_packages:
            user_package = AssetPackage(asset=asset, count=package.count)
            portfolio.append(user_package)
            price = self._market.find_price(asset)
            self._money_transfer(seller=package.portfolio,
                                 buyer=portfolio,
                                 amount=price * count)

    @staticmethod
    def _money_transfer(seller: Portfolio, buyer: Portfolio, amount: float):
        buyer.wallet.minus_amount(amount)
        seller.wallet.plus_amount(amount)
