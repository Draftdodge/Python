# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа.
# А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше,
# чем ваш уровень, вызывайте исключение уровня доступа.

from task4 import User, load_users
from task3 import LevelError, AccessError, ProjectExeption


class Project:
    def __init__(self, file_name):
        self.admin = None
        self.data = load_users(file_name)

    def auth(self, id_, name):
        temp_user = User(id_, None, name)
        if temp_user not in self.data:
            raise AccessError(temp_user)
        for user in self.data:
            if user == temp_user:
                self.admin = user

    def add_user(self, id_, level, name):
        if not self.admin:
            raise ProjectExeption
        if int(level) < int(self.admin.level):
            raise LevelError(level, self.admin.level)
        self.data.add(User(id_, level, name))


project = Project('task04.json')
project.auth("12345656", "Alex")
project.add_user("34234234", "8", "Igor")
print(project.data)
