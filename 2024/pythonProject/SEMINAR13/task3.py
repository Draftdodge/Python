# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
from SEMINAR13.task4 import User


class ProjectExeption(Exception):
    pass


class LevelError(ProjectExeption):
    def __init__(self, new_level, adm_level ):
        self.new_level = new_level
        self.adm_level = adm_level
    def __str__(self):
        return f'Уровень пользователя {self.new_level} ниже чем ваш {self.adm_level}'


class AccessError(ProjectExeption):
    def __init__(self, user : User):
            self.user = user

    def __str__(self):
            return f'Пользователя не существует'
