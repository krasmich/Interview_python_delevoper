"""
Задание 1

Создать два класса. Первый — родительский (ItemDiscount), должен содержать
статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре
в одной строке вида (“{название товара} {цена товара}”). Создать экземпляры родительского класса
и дочернего. Распечатать информацию о товаре.

"""


class ItemDiscount:
    """Родительский класс со статической информацией"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount для получения данных"""

    def get_parent_data(self):
        """Отображение информации о товаре в одну строку"""
        print(f'наименование товара: {self.name}, цена товара: {self.price}')


product = ItemDiscount('комплект лыж', 20000)
product_info = ItemDiscountReport(product.name, product.price)
product_info.get_parent_data()
