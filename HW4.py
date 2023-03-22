# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# import random
# import time
# len_first_set = 100 #int(input("Введите размер первого множества: "))
# len_second_set = 100 #int(input("Введите размер второго множества: "))
# first_set = set(random.randint(1,1500) for _ in range(0, len_first_set))
# second_set = set(random.randint(1,1500) for _ in range(0, len_second_set))
# third_set = first_set & second_set
# print(first_set)
# print(second_set)
# print(third_set)
# # сортировка перый способ
# start = time.perf_counter()
# print(sorted(list(third_set)))
# stop = time.perf_counter()
# res_time_1 = stop - start
# # сортировка второй способ
# start = time.perf_counter()
# list_third = list(third_set)
# temp = 0
# for j in range(0, len(list_third)):
#  for i in range(0, len(list_third)-1):
#   if list_third[i] > list_third[i+1]:
#     temp = list_third[i+1]
#     list_third[i+1] = list_third[i]
#     list_third[i]= temp
# print(list_third)
# stop = time .perf_counter()
# res_time_2 = stop - start
# print(res_time_2/res_time_1)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
number_bush = int(input("Введите количество кустов: "))
dict_ = {}
for i in range(0, number_bush):
 dict_[i] = random.randint(0,10)
print (dict_)
max_berry = dict_[number_bush - 1]+dict_[0]+dict_[1]
temp = 0
for i in range(0, number_bush-1):
 if i == number_bush-2:
  temp =dict_[i]+dict_[i + 1]+dict_[0]
 else:
  temp=dict_[i]+dict_[i + 1]+dict_[i + 2]
 if temp>max_berry :
  max_berry = temp
print(max_berry)