# Задача №55.  Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import function

while True:
    print('1 - вывод телефонного справочника, 2 - добавить запись, 3 - найти запись, 4 - удалить запись, 5 - редактировать запись')
    mode = int(input())
    if mode == 1:
        function.show_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    elif mode == 4:
        function.remove_data()
    elif mode == 5:
        function.edit_data()

    else:
        break

# with open("1.txt", "w", encoding="utf-8") as f:
#     f.write('ФИО | номер телефона')
#
#
# with open("1.txt", "r", encoding="utf-8") as f:
#     print(f.read())