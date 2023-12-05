from .asset import Asset


class AssetNotFound(Exception):

    def __init__(self, asset: Asset):
        self._asset = asset

    def __str__(self) -> str:
        return f'The {self._asset} is not found in list'


class NotEnoughAssets(Exception):

    def __init__(self, count: int) -> None:
        self._count = count

    def __str__(self) -> str:
        return f'There are less than {self._count} assets in package'


class CreateZeroPackage(Exception):
    """Исключение при создании пакета активов с 0 элементов"""

    def __str__(self) -> str:
        return 'Cannot create package with 0 count'
