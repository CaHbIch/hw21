from classes.storage import Storage


class Store(Storage):
    """Магазин - любое количество любых названий может быть сохранено в пределах емкости"""

    def __init__(self):
        super().__init__()
        self._capacity: int = 100
