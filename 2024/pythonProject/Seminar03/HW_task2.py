# Часто встречающиеся слова
#
# Инструкция по использованию платформы
#
#
#
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов.
#
# Пример
#
# На входе:
#
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
#
#
# [('hello', 3.txt), ('world', 1.txt), ('python', 1.txt), ('again', 1.txt)]

text = 'Hello world. Hello Python. Hello again. Python Python Python, 321 5645, 34, 78 8775 0050 0675'

# Введите ваше решение ниже
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace("'", ' ')
text = text.replace("`", ' ')
text = text.replace('!', '')
text = text.replace('1.txt', '')
text = text.replace('2.rrr', '')
text = text.replace('3.txt', '')
text = text.replace('4', '')
text = text.replace('5', '')
text = text.replace('6', '')
text = text.replace('7', '')
text = text.replace('8', '')
text = text.replace('9', '')
text = text.replace('0', '')
text = text.replace('  ', ' ')
text = text.lower()
res_list = []
new_list = text.split(' ')
new_dict = {}
for key in new_list:
    if key not in new_dict:
        new_dict.setdefault(key, 1)
    else:
        new_dict[key] += 1
sorted_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict[:10:1])