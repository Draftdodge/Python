# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
import os
from pathlib import Path
import shutil

def rename_files(desired_name, num_digits, source_ext, target_ext):
    os.chdir('test_folder')
    p = Path(Path().cwd())
    count = 1
    for obj in p.iterdir():
        ext = str(obj).split(".")[-1]
        if ext == source_ext:
            Path(obj).rename(f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}')
            count += 1

def create_file():
    shutil.rmtree('test_folder')
    Path('test_folder').mkdir()
    os.chdir('test_folder')
    for i in range(1, 12):
        with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
            pass

create_file()
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")