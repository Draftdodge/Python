# Задание №6 Погружение в Python | Коллекции Пользователь вводит строку текста.
# Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = 'jkasdhakj sakjda sdjac jaa jas lasd'
data = text.split(' ')
data.sort()
longest_word = len(max(data, key=len))
print(longest_word)
for n, s in enumerate(data, 1):
    # print(n, s.rjust(longest_word))
    print(f'{n} {s:>{longest_word}}')

