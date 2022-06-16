"""
Задание 5

Усовершенствовать программу «Банковский депозит». 
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. 
Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. 
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.

"""


dep_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
dep_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
dep_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
bank_deposits = [dep_1, dep_2, dep_3]


def calculate_deposit(amount, term, add_amount):
    """ Функция возвращает сумму вклада на конец срока c %
    :param amount: сумму вклада
    :param term: срок вклада
    :param add_amount: дополнительный вклад
    :return: сумма вклада на конец срока
    """

    def additional_funds():
        """ Функция возвращает сумму дополнительно внесенных средств c %
        :return: сумма дополнительных вкладов на конец срока
        """
        nonlocal add_amount, term
        add_amount += (add_amount * percent * ((term - 2) / 12))
        return add_amount * (term - 2)

    total_amount = 0
    for bank_deposit in bank_deposits:
        if bank_deposit['begin_sum'] <= amount < bank_deposit['end_sum']:
            total_amount = amount
            percent = bank_deposit[term] / 100

            total_amount += amount * percent * (term / 12)
            total_amount += additional_funds()
    if not total_amount:
            raise ValueError('Указана неправильная сумма вклада')
    return total_amount

print(calculate_deposit(10000, 6, 1000))
