# file_path = "C:/Users/User/Documents/example.txt"
# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os
file_path = "/Users/User/Documents/example.www.ee.txt"
def get_file_info(file_path: str):
    a, bc = os.path.split(file_path)
    b, c = os.path.splitext(bc)
    a = a + '/' if a else ''
    return (a, b, c)



def get_file_info_2(file_path: str):
    path_dir, file_name = file_path.split('.', 1)
    *path_dir_1, file_name_left = path_dir.split('/')
    path_dir_1 = f'{"/".join(path_dir_1)}{"/" if path_dir_1 else ""}'
    file_name_1 = f'{file_name_left}.{file_name}'
    *file_name_2, file_extention = file_name_1.split('.')
    file_name_res = f'{".".join(file_name_2)}'
    file_extention = f'.{file_extention}'
    return (path_dir_1, file_name_res, file_extention)


def get_file_info_3(file_path):
    file_name = file_path.split("/")[-1]
    print(file_name)
    file_extension = file_name.split(".")[-1]
    print(file_extension)
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

#print(get_file_info(file_path))
print(get_file_info_3(file_path))