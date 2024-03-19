import json
import os
import csv
import pickle
from os.path import join, getsize


def walk_in_directory(file_path=str):
    for root, dirs, files in os.walk(file_path):
        folder = root.split('\\')

        # это просмотр кто, что выдает
        print(f'В директории {folder[-1]}', end="\n")
        if not dirs:
            print("В этой папке нет директорий")
        else:

            print(f'Директория(и) {dirs}', end="\n")
        print(f'Файл(ы) {files}', end="\n")
        print(sum(getsize(join(root, name)) for name in files), end="\n")


        # запись в JSON file
        str_for_json = " ".join(files)
        to_json = {root: dirs, 'files': str_for_json, 'Size': sum(getsize(join(root, name)) for name in files) }
        with open('to_json.json', 'a') as f:
            json.dump(to_json, f, sort_keys=True, indent=2)

        # запись в CSV  file
        with open('for_csv.csv', 'a', newline='') as csvfile:
            fieldnames = ['files', 'dirs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'files': str_for_json, 'dirs': dirs})

        # запись в pickle  file
        with open('data.pickle', 'wb') as f:
            pickle.dump(to_json, f)

        with open('data.pickle', 'rb') as f:
            ...
            data_new = pickle.load(f)
        print(data_new)


walk_in_directory("C:\\Users\\Pavel\\Desktop\\study\\Python\\2024\\pythonProject\\seminar08\\")