"""
Задание 5

Проверить на практике возможности полиморфизма. Необходимо разделить
дочерний класс ItemDiscountReport на два класса. Инициализировать классы
необязательно. Внутри каждого поместить функцию get_info, которая в первом
классе будет отвечать за вывод названия товара, а вторая — его цены. Далее
реализовать вызов каждой из функции get_info.

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

    def __init__(self, name, price, disc_val):
        super().__init__(name, price)
        self.disc_val = disc_val

    def __str__(self):
        discount_price = self.price - self.price * self.disc_val * 0.01
        return f'цена товара со скидкой: {discount_price}'

    def get_parent_data(self):
        """Отображение информации о товаре в одну строку"""
        print(f'наименование товара: {self.name}, цена товара: {self.price}')


class ItemDiscountReportInfoName(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportInfoPrice(ItemDiscount):
    def get_info(self):
        print(self.price)


product1 = ItemDiscountReportInfoName('комплект лыж', 20000)
product2 = ItemDiscountReportInfoName('бритвы', 700)


def get_information(obj):
    obj.get_info()


def get_information_2(*args):
    for arg in args:
        arg.get_info()


get_information(product1)
get_information(product2)

get_information_2(product1, product2)

for obj in (product1, product2):
    obj.get_info()
