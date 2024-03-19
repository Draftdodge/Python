import csv
import os

# Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1.txt до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.


# Напишите функцию,
# которая сохраняет созданный в прошлом задании файл в формате CSV.
import json


def load_or_create(file_name):
    if file_name in os.listdir():
        with open(file_name, "r") as f:
            data = json.load(f)
        return data
    else:
        with open(file_name, "w") as f:
            json.dump({}, f)
        return {}


def enter_user(level, id, name, file_name):
    data = load_or_create(file_name)
    for value in data.values():
        if id in value:
            raise ValueError("id уже существует")
    data.setdefault(level, {})
    data[level].setdefault(id, name)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def json_to_csv(json_in: str, csv_out: str):
    with(
        open(json_in, "r", newline='', encoding="utf-8") as f_in,
        open(csv_out, "w", newline='', encoding="utf-8") as f_out,
    ):
        data = json.load(f_in)
        #        print(data)
        all_data = []
        csw_write = csv.DictWriter(f_out, fieldnames=["level", "id", "name"])
        for level, inner_dict in data.items():
            for id_, name in inner_dict.items():
                all_data.append({"id": id_, "level": level, "name": name})
        csw_write.writeheader()
        csw_write.writerows(all_data)


# level, id, name = list(input("введите level id name через пробел:").split(' '))
# enter_user(level, id, name, "task2.json")

if __name__ == '__main__':
    json_to_csv("task2.json", "task3.csw")
