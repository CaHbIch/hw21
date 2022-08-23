from abc import ABC

from classes.exception import StorageFull
from classes.storage import Storage


class Shop(Storage, ABC):
    """Магазин - любое количество до 5 наименований может храниться в пределах емкости"""

    def __init__(self):
        super().__init__()
        self._capacity: int = 20

    def add(self, title: str, quantity: int) -> None:
        """Увеличьте количество хранимых предметов """

        if self._get_unique_items_count() >= 5:
            raise StorageFull('В магазине нельзя хранить более 5 наименований товаров')
        super().add(title, quantity)
