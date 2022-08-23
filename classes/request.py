from typing import Tuple, Any

from classes.exception import MessageError


class Request:
    """Обрабатывать запросы на перемещение товара"""

    def __init__(self, storages: dict, message: str):
        """
        :param storages: Словарь с экземплярами Shop и Store
        :param message: Пример сообщение 'Доставить 3 печеньки из склад в магазин'
        """
        self._storages = storages
        self._message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        self._split_message(value)
        self._message = value

    @property
    def from_(self) -> str:
        return self._split_message(self.message)['from']

    @property
    def to(self) -> str:
        return self._split_message(self.message)['to']

    @property
    def product(self) -> str:
        return self._split_message(self.message)['product']

    @property
    def amount(self) -> int:
        return int(self._split_message(self.message)['amount'])

    @staticmethod
    def _split_message(message: str) -> dict:
        """Проверяет сообщение и получает поля из него

        :raises MessageError: Если передано некорректное сообщение
        """
        # Проверить длину
        message = message.split(' ')

        if len(message) < 7:
            raise MessageError('Некорректное сообщение')

        # Проверить поля fields
        split_message = {'from': message[4], 'to': message[6], 'amount': message[1], 'product': message[2]}
        if (
                split_message['from'] not in ['склад', 'магазин']
                or split_message['to'] not in ['склад', 'магазин']
                or not split_message['amount'].isdigit()
        ):
            raise MessageError('Вы ввели некорректное сообщение')

        return split_message

    def process(self) -> Tuple[Any, Any]:
        """Используйте методы хранилища для управления данными"""
        self._storages[self.from_].remove(self.product, self.amount)
        self._storages[self.to].add(self.product, self.amount)
        return self._storages[self.from_], self._storages[self.to]

    def __repr__(self):
        return f'from: {self.from_}, to: {self.to}, amount: {self.amount}, product: {self.product}'
