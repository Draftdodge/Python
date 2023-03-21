# Урок 3. Списки и словари
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# import time
# input_list = []
# list_len = int(input("Введите количество элементов в списке: "))
# for i in range(list_len):
#     input_list.append(int(input(f"Введите {i+1} элемент массива: ")))
# print(input_list)
# find_number = int(input("Введите число, которое необходимо найти: "))
# count = 0
# start = time.perf_counter()
# for i in range(list_len):
#     if input_list[i] == find_number :
#         count += 1
# stop = time.perf_counter()
# metod_1_time = stop - start
# print(f"Число {find_number} встречается {count} раз.")
# print(f"Потребовалось времени {metod_1_time}.")
# start = time.perf_counter()
# count = input_list.count(find_number)
# stop = time.perf_counter()
# metod_2_time = stop - start
# print(f"Число {find_number} встречается {count} раз.")
# print(f"Потребовалось времени {metod_2_time}.")
# print(f"метод Count() быстрее в {metod_1_time/metod_2_time} раз.")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
# import random

# list_len = int(input("Введите количество элементов в списке: "))
# input_list = [random.randint(1, 50) for _ in range(list_len)]
# find_number = int(input("Введите число, которое необходимо найти: "))
# input_list = list(set(input_list))
# print(input_list)
# d = 1
# while True:
#     if find_number - d in input_list:
#         number = find_number - d
#         break
#     elif find_number + d in input_list:
#         number = find_number + d
#         break
#     d += 1
# print(f" Ближайшее число r {find_number} - {number}")


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12


word_str = str(input("Введите слово: ")).upper()
dict_ = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
         'D': 2, 'G': 2,
         'B': 3, 'C': 3, 'M': 3, 'P': 3,
         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
         'K': 6,
         'J': 8, 'X': 8,
         'Q': 10, 'Z': 10}
summ = 0
print(word_str)
for i in range(len(word_str)):
    summ += dict_[word_str[i]]
print(summ)
