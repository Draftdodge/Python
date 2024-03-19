# Напишите программу, которая использует модуль logging
# для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='dbz.log', encoding='utf-8', level=logging.DEBUG)

def division(a: int | float, b: int | float):
    try:
        res = a / b
        logging.debug(f' x/y = {res}')
        return res
    except ZeroDivisionError as err:
        logging.error(f'{err}: На ноль делить нельзя')


if __name__ == '__main__':
    division(2, 7)
