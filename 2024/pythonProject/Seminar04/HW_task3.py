# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(1.5) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount_):
    if amount_ % MULTIPLICITY == 0:
        return True
    else:
        return print('Сумма должна быть кратной 50 у.е.')


def deposit(amount: int):
    global count
    if check_multiplicity(amount):
        count += amount
        return operations.append(f'Пополнение карты на {amount} у.е. Итого {count} у.е.')



def withdraw(amount: int):
    global count
    commision = int(min(max(amount * PERCENT_DEPOSIT, MIN_REMOVAL), MAX_REMOVAL))
    if count - amount > 0:
        if check_multiplicity(amount):
            count -= (amount + commision)
            return operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {commision} у.е.. Итого {count} у.е.')
    else:
        check_multiplicity(amount)
        return operations.append(f'Недостаточно средств. Сумма с комиссией {amount + commision} у.е. На карте {count} у.е.')


def exit():
    global count
    if count > RICHNESS_SUM:
        commision = count * RICHNESS_PERCENT
        count = count - commision
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {commision}000 у.е. Итого {count}000 у.е.')
        return operations.append(f'Возьмите карту на которой {count}000 у.е.')
    return operations.append(f'Возьмите карту на которой {count} у.е.')


deposit(173)
withdraw(21)
exit()
print(operations)
