# Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды.
lst = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, ]

for i in set(lst):
    counter = lst.count(i)
    if counter > 1:
        for _ in range(counter):
            lst.remove(i)

print(lst)