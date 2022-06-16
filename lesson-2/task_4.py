"""
Задание 4

Реализовать расчет цены товара со скидкой. Величина скидки должна
передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку
методов конструктора дочернего класса (метод __init__, в который должна
передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы (вторая и третья строка после объявления дочернего класса).

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


product = ItemDiscount('комплект лыж', 20000)
print(product.name, product.price)

product.name, product.price = 'ноутбук Razor', 150000

product_info = ItemDiscountReport(product.name, product.price, 50)
product_info.get_parent_data()

print((str(product_info)))
