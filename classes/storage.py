from abc import ABC, abstractmethod

from classes.exception import StorageFull, ItemsNotFound


class Storage(ABC):
    """ Класс абстракции Хранилища"""

    @abstractmethod
    def __init__(self):
        self._items = {}
        self._capacity: int = 0

    def __repr__(self):
        return f'Это Storage типа {self.__class__.__name__} с емкостью {self._capacity}'

    def add(self, title: str, count: int) -> None:
        """ Увеличивает запас items """
        if self._get_free_space() < count:
            raise StorageFull('Нет свободного места')
        self._items[title] = self._items.get(title, 0) + count

    def remove(self, title: str, count: int) -> None:
        """  Уменьшает запас items """
        if title not in self._items.keys():
            raise ItemsNotFound(f'Товар с наименованием {title} не найден')
        if count > self._items.get(title):
            raise ItemsNotFound(f'Нет нужного количества товара с наименованием {title}')

        self._items[title] = self._items.get(title) - count
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self):
        """ Возвращает количество свободных мест """
        taken_space = sum([item for item in self._items.values()])
        return self._capacity - taken_space

    def get_items(self) -> dict:
        """  Возвращает содержание хранилища"""
        return self._items

    def _get_unique_items_count(self) -> int:
        """ Возвращает количество уникальных товаров. """
        return len([item for item in self._items.keys()])
