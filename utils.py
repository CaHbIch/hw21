from sys import exit
from typing import Tuple, List

from classes import Shop, Store, Request, MessageError, StorageFull, ItemsNotFound


def create_instances(goods_shop: List[Tuple[str, int]], goods_store: List[Tuple[str, int]]) -> [Shop, Store]:
    """Создание и заполнение экземпляров хранилища"""
    shop = Shop()
    for item in goods_shop:
        shop.add(*item)

    store = Store()
    for item in goods_store:
        store.add(*item)

    return shop, store


def display_items(shop: Shop, store: Store) -> str:
    """"Создает сообщение с сохраненными элементами"""
    header_store = 'В склад хранится:\n'
    header_shop = '\nВ магазин хранится:\n'
    return (header_store
            + '\n'.join([f'{value} {key}' for key, value in store.get_items().items()])
            + '\n'
            + header_shop
            + '\n'.join([f'{value} {key}' for key, value in shop.get_items().items()]))


def send_request(user_task: str, shop: Shop, store: Store) -> str:
    """Отправить запрос и вернуть процесс выполнения"""
    if user_task.lower() == 'стоп':
        exit()
    try:
        request = Request({'магазин': shop, 'склад': store}, user_task)
        request.process()
        return (f'\nЗапрос принят, товар в нужном количестве имеется\n'
                f'Курьер доставил {request.amount} {request.product} из {request.from_} в {request.to}\n')
    except (MessageError, StorageFull, ItemsNotFound) as e:
        print(e)
        user_task = input('Попробуйте еще раз: ')
        send_request(user_task, shop, store)
