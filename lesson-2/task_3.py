"""
Задание 3

Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.

"""


class ItemDiscount:
    """Родительский класс со статической информацией"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount для получения данных"""

    def get_parent_data(self):
        """Отображение информации о товаре в одну строку"""
        print(f'наименование товара: {self.name}, цена товара: {self.price}')


product = ItemDiscount('комплект лыж', 20000)
print(product.name, product.price)

product.name, product.price = 'ноутбук Razor', 150000

product_info = ItemDiscountReport(product.name, product.price)
product_info.get_parent_data()
