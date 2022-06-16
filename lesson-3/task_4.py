"""
Задание 4

Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
"""
import random
import string
from os import getcwd
from os.path import join


def create_text_file(file_name, length=100):
    """Функция создает текстовый файл из рандомных букв и цифр
    :param file_name: имя файла
    :param length: количество строк
    """
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for _ in range(length))
            texts_list = [letter * 23 for letter in rand_string]

            nums_list = [random.randint(0, 10000000000) for _ in range(length)]

            texts_nums_zip = zip(texts_list, nums_list)

            for el in texts_nums_zip:
                file.write(f'{el[0]} {el[1]}\n')
    except FileExistsError:
        print('Файл уже существует!')
    finally:
        file_output(join(getcwd(), file_name))


def file_output(path):
    """Построчный вывод содержимого файла
    :param path: абсолютный путь файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)


create_text_file('task_4.txt')
