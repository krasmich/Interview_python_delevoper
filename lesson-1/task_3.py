"""
Задание 3 

Разработать целочисленный генератор случайных чисел. 
В функцию передавать начальную и конечную границу диапазона генерации (выдавать значения из диапазона включая концы). 
Заполнить этими данными словарь. 
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, а значение сгенеренное случайное число.  
Вывести содержимое словаря. 
"""

from random import randint


def generator_numbers(start, end):
    """ Генерирует рандомные числа
    :param start: стартовая позиция
    :param end: конечная позиция
    """
    values = [randint(start, end) for i in range(5)]

    dict_random = {}
    for index, value in enumerate(values):
        dict_random[f'elem_{index}'] = value
    
    print(dict_random)


generator_numbers(1, 100)
