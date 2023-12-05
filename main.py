from assets.asset_package import AssetPackage
from market.default import YANDEX_ASSET, VK_ASSET
from market.market import Market
from portfolio.portfolio import Portfolio
from regulator.regulator import Regulator


def main():
    market = Market()
    vasya = Portfolio(name='Вася')
    vasya.wallet.plus_amount(5000)
    sasha = Portfolio(name='Саша')
    sasha.wallet.plus_amount(50)
    yandex_package = AssetPackage(asset=YANDEX_ASSET, count=20)
    sasha.append(yandex_package)
    vk_package = AssetPackage(asset=VK_ASSET, count=5)
    vasya.append(vk_package)
    print(f'Vasya cost: {vasya.current_cost}')
    print(f'Vasya wallet: {vasya.wallet.amount}')
    print(f'Sasha cost: {sasha.current_cost}')
    print(f'Sasha wallet: {sasha.wallet.amount}')
    regulator = Regulator(market=market)
    regulator.from_portfolio_to_market(portfolio=sasha,
                                       asset=YANDEX_ASSET,
                                       count=10)
    print('> Move 10 yandex from Sasha to market')
    print(f'Vasya cost: {vasya.current_cost}')
    print(f'Vasya wallet: {vasya.wallet.amount}')
    print(f'Sasha cost: {sasha.current_cost}')
    print(f'Sasha wallet: {sasha.wallet.amount}')
    market.show_stock()
    regulator.from_market_to_portfolio(portfolio=vasya,
                                       asset=YANDEX_ASSET,
                                       count=5)
    print('> Vasya buy 5 yandex assets')
    print(f'Vasya cost: {vasya.current_cost}')
    print(f'Vasya wallet: {vasya.wallet.amount}')
    print(f'Sasha cost: {sasha.current_cost}')
    print(f'Sasha wallet: {sasha.wallet.amount}')
    market.show_stock()


if __name__ == '__main__':
    main()
