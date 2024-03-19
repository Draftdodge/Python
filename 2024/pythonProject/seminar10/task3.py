# Задание №3.txt 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

# Задание №4 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть: ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
class DataPerson:

    def __init__(self, name: str, sername: str, age: int):
        self.name = name
        self.sername = sername
        self.__age = age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.name} {self.sername} {self.__age}"


class Worker(DataPerson):
    def __init__(self, id: int = 1, *args, **kwargs):
        if len(str(id)) != 6:
            raise ValueError('Некорректный номер')
        self.id = id
        self.level = sum(map(int, str(id))) % 7
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    w = Worker(1234662, 'Alex', 'pus', 22)
    print(f'{w.id=}, {w.level=}')

    human_1 = DataPerson('Petr', 'Petrov', 27)
    human_2 = DataPerson('Sergey', 'Serov', 30)

    print(human_1)
    print(human_2)
"""
class Employee(DataPerson):
    def __init__(self, name: str, sername: str, age: int, emp_id: int = 1.txt):
        if len(str(emp_id)) != 6:
            raise ValueError('Некорректный идентификационный номер')
        self.emp_id = emp_id
        self.level = sum(map(int, str(emp_id))) % 7
        super().__init__(name, sername, age)


if __name__ == '__main__':
    e = Employee('Александр', 'Пушкин', 19, 123321)
    print(f'{e.emp_id=}, {e.level=}')
"""
