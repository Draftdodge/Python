# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

numbers = [13, 2, 3, 5, 7, 2, 5]
odd_indexes = []
for i, elem in enumerate(numbers, 1):
    if elem % 2 != 0:
        odd_indexes.append(i)

print(odd_indexes)

odd_indexes = [index + 1 for index, num in enumerate(my_list) if num % 2 != 0]