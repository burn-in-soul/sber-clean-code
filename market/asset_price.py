from assets.asset import Asset

SBER_ASSET = Asset('sber')
GAZPROM_ASSET = Asset('gazprom')
VK_ASSET = Asset('vk')
YANDEX_ASSET = Asset('yandex')


class AssetPrice(dict):
    """Заглушка для хранения. Должна быть внешняя система хранения"""
    def __init__(self):
        super().__init__()
        self.__dict__[SBER_ASSET.name] = 100.4
        self.__dict__[GAZPROM_ASSET.name] = 22.1
        self.__dict__[VK_ASSET.name] = 502.4
        self.__dict__[YANDEX_ASSET.name] = 1000

    def __setitem__(self, asset: Asset, price: float):
        self.__dict__[asset.name] = price

    def __getitem__(self, asset: Asset) -> float:
        return self.__dict__[asset.name]
