"""
Задание 3

Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Если есть  значения, которым не хватило ключей, их необходимо отбросить.
"""


def create_dict(keys, values):
    """Создание словаря из 2-x списков
    :param keys: список с ключами
    :param values: список со значениями
    """
    len_keys = len(keys)
    len_values = len(values)
    if len_values < len_keys:
        values_copy = values[:]
        for _ in range(len_keys - len_values):
            values_copy.append(None)
        new_dict = {key: value for key, value in zip(keys, values_copy)}
    else:
        new_dict = {key: value for key, value in zip(keys, values)}
    return new_dict


keys_list = ['q', 'w', 'e', 'r', 't', 'y']
values_list = [1, 2, 3, 4, 5]
print(create_dict(keys_list, values_list))
