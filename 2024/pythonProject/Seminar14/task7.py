import json
import os


class User:
    def __init__(self, id_: str, level: str, name: str):
        self.id, self.level, self.name = id_, level, name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'User({self.id}, {self.level}, {self.name})'


class ProjectExeption(Exception):
    pass


class LevelError(ProjectExeption):
    def __init__(self, new_level, adm_level):
        self.new_level = new_level
        self.adm_level = adm_level

    def __str__(self):
        return f'Уровень пользователя {self.new_level} ниже чем ваш {self.adm_level}'


class AccessError(ProjectExeption):
    def __init__(self, user: User):
        self.user = user

    def __str__(self):
        return f'Пользователя не существует'


def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    with open(file_name, 'w') as f:
        json.dump({}, f)
    return {}


def enter_users(level: str, id_: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id_ in value:
            print("id уже существует")

    data.setdefault(level, {})
    data[level].setdefault(id_, name)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return


def load_users(file_name: str) -> set[User]:
    data = load_or_create(file_name)
    res = set()
    for level, v in data.items():
        for id_, name in v.items():
            res.add(User(id_, level, name))
    return res


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


import pytest


@pytest.fixture
def auth_project(request):
    file = 'test_users.json'
    data = {"5": {"12345656": "Alex"}, "7": {"12345657": "Ben"}}
    with open(file, 'w') as f:
        json.dump(data, f)
    p = Project(file)
    p.auth("12345656", "Alex")
    def delete_project():
        os.remove(file)
    request.addfinalizer(delete_project)
    return p


@pytest.fixture
def auth_user():
    return User('12345656', '5', 'Alex')

def test_user_authed(auth_project, auth_user):
    assert auth_project.admin is not None
    assert auth_project.admin == auth_user



if __name__ == '__main__':
    pytest.main()

    # enter_users('5', '12345656', 'Alex', 'task04.json')
    # enter_users('7', '12345657', 'Ben', 'task04.json')
    # print(load_users('task04.json'))
    # project = Project('task04.json')
    # project.auth("12345656", "Alex")
    # project.add_user("34234234", "8", "Igor")
    # print(project.data)

