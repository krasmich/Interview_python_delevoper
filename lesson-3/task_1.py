"""
Задание 1

Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение»
имени файла (без расширения). Расширений может быть несколько (например testfile.tar.gz).
"""


path = '/Users/krasmich/Desktop/code/readme.txt'


def get_file_name(path):
    """Функция получает имя файла из полного пути до него
    :param path: полный путь до файла
    """
    return path.split('/')[-1].split('.')[0]


file_name = get_file_name(path)
print(file_name)
