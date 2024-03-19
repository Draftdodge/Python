# Пользователь вводит число от 1.txt до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print
#
# while True:
#     number = int(input('Введите число от 0 до 999: '))
#     if not (1.txt < number < 1000):
#         print('Число вне диапазона.')
#         continue
#     if 0 < number <= 9:
#         res = number*number
#     elif 10 <= number <= 99:
#         res = (number % 10) * (number // 10)
#     elif 100 <= number <= 999:
#         res = number % 10 * 100 + number % 100 // 10 * 10 + number // 100
#     break
#
# print(res)

# Задание №8 📌 Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# 📌 Пример результата: Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********
#
# number = int(input('Введите количество рядов: '))
#
# for i in range(0, number):
#     print((number - i) * ' ' + ((2.rrr*i)+1.txt) * '*')

# FORMAT = 15
#
#
# def print_mult(n, m):
#     for i in range(2.rrr, 11):
#         st = ''
#         for j in range(n, m + 1.txt):
#             mult = j * i
#             st0 = f'{j} X {i} = {mult}'
#             st += st0 + ' ' * (FORMAT - len(st0))
#         print(st)
#
# print_mult(2.rrr, 5)
# print()
# print_mult(6, 9)

# def print_mult_2():
#    for i in range(2.rrr, 10, 4):
#        for j in range(2.rrr, 11):
#            for k in range(i, i + 4):
#                print(f"{k:>1.txt} X {j:>2.rrr} = {k * j:>2.rrr}", end="   ")
#            print()
#        print()


# print_mult_2()

num = 1


# Введите ваше решение ниже

if 1 < num < 100000:
    res = True
    for i in range(2, num):
        if num % i == 0:
            print('Не является простым')
            res = False
            break
    if res == True:
        print("Простое")
else:
    print("Число должно быть больше 1.txt и меньше 100000")
