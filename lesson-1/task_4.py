"""
Задание 4

Написать программу «Банковский депозит». 
Клиент банка делает депозит на определенный срок. 

В зависимости от суммы и срока вклада определяется процентная ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых). 

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: 
сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока.
"""

dep_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
dep_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
dep_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
bank_deposits = [dep_1, dep_2, dep_3]


def calculate_deposit(amount, term):
    """ Функция возвращает сумму вклада на конец срока c %
    :param amount: сумму вклада
    :param term: срок вклада
    :return: сумма вклада на конец срока
    """
    total_amount = 0
    for bank_deposit in bank_deposits:
        if bank_deposit['begin_sum'] <= amount < bank_deposit['end_sum']:
            total_amount = amount
            percent = bank_deposit[term] / 100

            total_amount += amount * percent * (term / 12)
    if not total_amount:
            raise ValueError('Указана неправильная сумма вклада')
    return total_amount


print(calculate_deposit(10000, 24))