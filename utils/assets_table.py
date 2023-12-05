from tabulate import tabulate

from default.asset_package_list.abc_asset_package_list import PackageList
from market.default import prices


class AssetsTable:
    """Таблица активов для вывода"""

    def __init__(self, package_list: PackageList) -> None:
        self._package_list = package_list

    def create(self) -> str:
        headers = ['Актив', 'Цена', 'Количество']
        data = [[package.asset,
                 prices[package.asset],
                 package.count] for package in self._package_list]
        return tabulate(tabular_data=data, headers=headers, tablefmt='orgtbl')
