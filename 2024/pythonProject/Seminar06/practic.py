# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина,
# а если попытки исчерпаны - ложь.

# Добавьте возможность запуска функции “угадайки”
# из модуля в командной строке терминала.
# Строка должна принимать от 1.txt до 3.txt аргументов:
# параметры вызова функции. Для преобразования строковых
# аргументов командной строки в числовые параметры используйте
# генераторное выражение.

import random
import sys


def guess(min_number, max_number=10, count=3) -> bool:
    magic_number = random.randint(min_number, max_number)
    for _ in range(0, count):
        number = int(input(f'Введите число от {min_number} до {max_number}: '))
        if number < magic_number:
            print(f'введенное число {number} < загадонного')
        elif number > magic_number:
            print(f'введенное число {number} > загадонного')
        else:
            print('Угадали!!!')
            return True
    print("Попытки кончились. Это было: ", magic_number)
    return False


print(sys.argv)
_, min, max, c = list(map(int, sys.argv[1:]))

if __name__ == '__main__':
    print(guess(*list(map(int, sys.argv[1:]))))
    guess(min, max, c)

