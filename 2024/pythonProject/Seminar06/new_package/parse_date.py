# Создайте модуль и напишите в нём функцию,
# которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь,
# если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1.txt, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
__all__ = ['is_date_valid']

__MOUNTHS = {1: range(1, 32),
             2: range(1, 29),
             3: range(1, 32),
             4: range(1, 31),
             5: range(1, 32),
             6: range(1, 31),
             7: range(1, 32),
             8: range(1, 32),
             9: range(1, 31),
             10: range(1, 32),
             11: range(1, 31),
             12: range(1, 32), }


def _is_valid_year(year: int) -> bool:
    return year in range(1, 10000)


def _is_valid_mounth(mounth: int) -> bool:
    return mounth in range(1, 13)


def _is_valid_day(day: int, mounth: int, year: int) -> bool:
    if _leap_year(year) and mounth == 2:
        return day in range(1, 30)
    return day in __MOUNTHS[mounth]


def _leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def is_date_valid(data: str) -> bool:
    print(data)
    d, m, y = map(int, data.split('.'))
    print(d, m, y)
    if _is_valid_year(y) and _is_valid_mounth(m) and _is_valid_day(d, m, y):
        return True
    return False

date_to_prove = '11.01.2022'
print(is_date_valid(date_to_prove))
