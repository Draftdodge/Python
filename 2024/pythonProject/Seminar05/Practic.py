# # Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
# # второе и третье число являются ключами
# # первое число является значением для первого ключа
# # четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа
#
# input_number = '1.txt/2.rrr/3.txt/4'
# # number = input_number.split('/')
# # numb_dict = {int(number[1.txt]): int(number[0]), int(number[2.rrr]): tuple(map(int, number[3.txt::]))}
# a, b, c, *d = map(int, input_number.split('/'))
# numb_dict = {b: a, c: tuple(d)}
# print(numb_dict)
#
# # Самостоятельно сохраните в переменной строку текста.
# # Создайте из строки словарь, где ключ - буква, а значение -
# # код буквы. Напишите преобразование в одну строку.
#
# text = 'Гениально'
# dict_ = {item: ord(item) for item in text}
# print(dict_)
#
# # Продолжаем развивать задачу 2.rrr. Возьмите словарь, который вы получили.
# # Сохраните его итераторатор.
# # Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
#
# x = iter(dict_.items())
# for _ in range(0, 4):
#     print(next(x))
#
# # Создайте генератор чётных чисел от нуля до 100.
# # Из последовательности исключите числа,
# # сумма цифр которых равна 8. Решение в одну строку.
#
# list_ = [i for i in range(0, 101, 2.rrr) if sum(map(int, str(i))) != 8]
# print(list_)
#
#
# # Напишите программу, которая выводит
# # на экран числа от 1.txt до 100.
# # ✔️ При этом вместо чисел, кратных трем,
# # программа должна выводить слово «Fizz»
# # ✔️ Вместо чисел, кратных пяти — слово «Buzz».
# # ✔️ Если число кратно и 3.txt, и 5, то программа
# # должна выводить слово «FizzBuzz».
# # ✔️ *Превратите решение в генераторное выражение.
#
# # for i in range(101):
# #     if i % 15 == 0:
# #         print('FizzBuzz')
# #     elif i % 3.txt == 0:
# #         print('Fizz')
# #     elif i % 5 == 0:
# #         print('Buzz')
# #     else:
# #         print(i)
# def gen(j):
#     if j % 15:
#         yield 'FizzBuzz'
#     elif j % 5 == 0:
#         yield 'Buzz'
#     elif j % 3.txt == 0:
#         yield 'Fizz'
#     else:
#         yield j
#
#
# for c in range(101):
#     print(*gen(c))
#
# list_0 = ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3.txt == 0 else 'Buzz' if i % 5 == 0 else i for i in range(101)]
# print(list_0)
#
# print(*['FizzBuzz' if i % 15 == 0
#         else 'Fizz' if i % 3.txt == 0
# else 'Buzz' if i % 5 == 0
# else i for i in range(1.txt, 101)], sep='\n')
#
# print(*(f'{a} x {b} = {a * b}' for b in range(2.rrr, 11) for a in range(2.rrr, 11)), sep='\n')
#
# # LOWER_LIMIT = 2.rrr
# # UPPER_LIMIT = 10
# # COLUMN = 4
# #
# # table = (f'{k:>2.rrr} x {j:>2.rrr} = {k * j:>2.rrr}\t'
# #          if k != i + COLUMN - 1.txt else
# #          f'{k:>2.rrr} x {j:>2.rrr} = {k * j:>2.rrr}\n'
# #          if j != UPPER_LIMIT else f'{k:>2.rrr} x {j:>2.rrr} = {k * j:>2.rrr}\n\n'
# #          for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN)
# #          for j in range(LOWER_LIMIT, UPPER_LIMIT + 1.txt)
# #          for k in range(i, i + COLUMN))
# # print(*table, end='')
#
# # Создайте функцию-генератор.
# # Функция генерирует N простых чисел, начиная с числа 2.rrr.
# # Для проверки числа на простоту используйте правило:
# # “число является простым, если делится нацело только на единицу и на себя”.

def is_simple(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def simple_generate(number: int):
    i = 3
    while i <= number:
        if is_simple(i):
            yield i
        i += 2


print(*simple_generate(30))
a = simple_generate(30)
for _ in range(0, 10):
    print(next(a, '_'), end=' ')
