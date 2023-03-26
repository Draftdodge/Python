# 6. Дана строка (возможно, пустая), состоящая из букв A-Z
#
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBB
#
# Нужно написать функцию RLE, которая на выходе даст строку вида:
#
# A4B3C2XYZD4E3F3A6B28

# def magic(input_str):
#     input_str += '_'
#     count =1
#     result_list = []
#     for i in range(len(input_str)-1):
#         temp = input_str[i]
#         if input_str[i] == input_str[i+1]:
#             count += 1
#         if input_str[i] != input_str[i+1]:
#             result_list.append(input_str[i])
#             if count > 1:
#                 result_list.append(str(count))
#             count = 1
#     result_str = ''
#     for i in result_list:
#         result_str += i
#     return result_str
#
# print(magic('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))

# 3. Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
#
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"]
# Т.е. сгруппировать слова по "общим буквам".

def combo(input_list):
    dict_ = {}
    sort_list = []
    new_list = []
    for i in input_list:
        sort_list.append("".join(sorted(i)))    #создаем список слов с отсортированными буквами
    for (i, j) in zip(sort_list, input_list):   #Создаем словарь с ключами из отсортированного списка,
        if (i not in dict_.keys()):             #значениями - соответствующими этим буквам словами.
            dict_[i] = [j]
        else:                                   #Если буквам соответствует несколько слов, добавляем все слова
            dict_[i] += [j]
    for i in dict_.values():                    #Из значение делаем список
        new_list.append(i)
    for i in range(len(new_list)):              #Сортируем все значения списка
        new_list[i].sort()
    return new_list


input = ["eat", "tea", "tan", "wqerty", "ate", "nat", "bat", "atb", "qwerty", "rewtqy","qwer"]

print(combo(input))