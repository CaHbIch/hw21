from sys import exit

from classes import goods_shop, goods_store
from utils import send_request, display_items, create_instances


def main():
    # Стартовое сообщение и запрос на ввод
    print('Привет! Программа симулирует движение товаров между складом и магазином\n'
          '\nДля отправки товаров нужно ввести сообщение\n'
          'Формат: Доставить [кол-во] [наименование] из [откуда] в [куда]\n'
          'Пример: Доставить 2 слон из склад в магазин\n'
          '\nДля остановки программы в любой момент введите "стоп"\n'
          'Для начала работы нажмите Enter')
    user_input = input()

    if user_input == 'стоп':
        exit()

    # Создание и заполнение экземпляров Магазина и склада
    shop, store = create_instances(goods_shop, goods_store)

    while True:
        # Отображать товары на складе и магазине
        print(display_items(store=store, shop=shop))

        # Запрашивать ввод пользователя и обрабатывать его
        user_task = input('\nВведите задание: ')
        print(send_request(user_task, shop, store))


if __name__ == '__main__':
    main()
