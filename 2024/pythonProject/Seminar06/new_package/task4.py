# Создайте модуль с функцией внутри.
# Функция получает на вход загадку,
# список с возможными вариантами отгадок и
# количество попыток на угадывание.
# Программа возвращает номер попытки,
# с которой была отгадана загадка или ноль, если попытки исчерпаны.


# 'Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна']

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию,
# чтобы передать ей все свои загадки.
#
# Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражениеlte

_result = dict()


def secret(riddle: str, answer: list[str], count: int) -> int:
    print(riddle)
    for i in range(1, count + 1):
        ans = input('Введите ответ: ')
        if ans in answer:
            answer_counter(riddle, i)
            return i
    answer_counter(riddle, 0)
    return 0


def test_storage():
    dict_riddle = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                   'Не лает, не кусает, в дом не пускает': ['замок'],
                   'Сидит дед во сто шуб одет': ['лук', 'луковица'], }
    for test_data in dict_riddle.items():
        secret(*test_data, 3)


def answer_counter(riddle: str, count):
    global _result
    _result.setdefault(riddle, count)


def print_result():
    global _result
    for k, v in _result.items():
        print(f'{k=} {v=}')


if __name__ == '__main__':
    test_storage()
    print_result()

#    print(secret('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'], 3.txt))
