class StorageFull(Exception):
    """Возвращает сообщение когда не осталось места"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ItemsNotFound(Exception):
    """В случае, если не сохраненное название передано или запрошенное количество превышает сохраненное"""

    def __init__(self, message='Товар не найден'):
        self.message = message
        super().__init__(message)


class MessageError(Exception):
    """Если передано неправильное сообщение"""

    def __init__(self, message='Неправильное сообщение'):
        self.message = message
        super().__init__(message)
