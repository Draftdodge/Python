# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.1

# first_elem = int(input("Введите первый элемент: "))
# difference = int(input("Введите разность: "))
# count_of_number = int(input("Введите количество элементов: "))
#
#
# def magic(first, dif, coun):
#     array = []
#     for i in range(1, coun + 1):
#         array.append(first + (i - 1) * dif)
#     return array
#
# print(magic(first_elem, difference, count_of_number))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

min_number = 20
max_number = 50

array = [random.randint(0, 70) for i in range(0, 10)]
index_array = []
for i in range(len(array)):
    if ((array[i] < max_number) and (array[i] > min_number)):
        index_array.append(i)
print(array)
print(index_array)