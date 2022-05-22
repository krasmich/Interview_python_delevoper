"""
Задание 2

Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
что при сохранении текущей логики работы программы будет сгенерирована ошибка
выполнения. Усовершенствовать родительский класс таким образом, чтобы получить доступ к
защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.

"""


class ItemDiscount:
    """Родительский класс со статической информацией"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount для получения данных"""

    def get_parent_data(self):
        """Отображение информации о товаре в одну строку"""
        print(f'наименование товара: {self.name}, цена товара: {self.price}')


product = ItemDiscount('комплект лыж', 20000)
product_info = ItemDiscountReport(product.name, product.price)
product_info.get_parent_data()

# AttributeError: 'ItemDiscount' object has no attribute 'name'
