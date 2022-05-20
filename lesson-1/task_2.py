"""
Задание 2

Реализовать функцию print_directory_contents(path). 
Функция принимает имя директории и выводит ее содержимое, 
включая содержимое всех поддиректории (рекурсивно вызывая саму себя). 
Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""

import os

s_path = '/home/krasmich/Interview_python_delevoper'


def print_directory_contents(s_path):
    """ Функция принимает имя директории и выводит ее содержимое, 
    включая содержимое всех поддиректории.
    :param s_path: путь до каталога
    """
    print('Content', os.listdir(s_path))
    for i in os.listdir(s_path):
        if os.path.isdir(i):
            print('Заходим', i)
            print_directory_contents(i)
            print('Возвращаемся в', s_path)


print_directory_contents(s_path)
