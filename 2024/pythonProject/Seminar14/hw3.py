import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        >>> e2 = Employee('Ivanov', 'Ivan','Ivanovich', 30, "manager", 50000)
        >>> e2.birthday()
        >>> e2.get_age()
        31
        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    """
    >>> e1 = Employee('Ivanov', 'Ivan','Ivanovich', 30, "manager", 50000)
    >>> e1.full_name()
    'Ivanov Ivan Ivanovich'
    """
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        """
        >>> e3 = Employee('ivanov', 'ivan','ivanovich', 30, "manager", 50000)
        >>> e3.last_name
        'Ivanov'
        """
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        """
        >>> e3 = Employee('Ivanov', 'Ivan','Ivanovich', 30, "manager", 50000)
        >>> e3.raise_salary(10)
        >>> e3.salary
        55000.0
        """
        self.salary *= (1 + percent / 100)

    def __str__(self):
        """
        >>> e3 = Employee('Ivanov', 'Ivan','Ivanovich', 30, "manager", 50000)
        >>> e3.__str__()
        'Ivanov Ivan Ivanovich (Manager)'
        """
        return f'{self.full_name()} ({self.position})'

# Введите ваше решение ниже
def test_employee_raise_salary():
    """
    >>> emp = Employee('Ivanov', 'Ivan','Ivanovich', 30, "manager", 50000)
    >>> emp.raise_salary(10)
    >>> emp.salary
    55000.0
    """
    pass


doctest.testmod(verbose=False)