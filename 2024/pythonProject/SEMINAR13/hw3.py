
class InvalidNameError(BaseException):
    def __str__(self):
        return f'Invalid name: . Name should be a non-empty string.'


class InvalidAgeError(BaseException):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(BaseException):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, name: str, surname: str, father_name, age):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.__age = age
        if not self.name or not self.surname or not self.father_name:
            raise InvalidNameError
        if self.__age < 1:
            raise InvalidAgeError(self.__age)

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

class Employee(Person):
    def __init__(self, name: str, surname: str, father_name, age, id_num):
        self.id_num = id_num
        if self.id_num > 999999 or self.id_num < 100000:
            raise InvalidIdError(self.id_num)

    def get_level(self):
        return sum(map(int, self.id_num)) % 7


if __name__ == '__main__':
    human_1 = Person('Petr', 'www', 'Pet222rov', 1)
    human_2 = Person('Sergey', 'Serov', 'Petrowewewv', 30)
    emp1 = Employee('www', 'wwwww', 'wwwww', 25, 233333)
    emp2 = Employee('eee', 'weeeww', 'eweew', 20, 2356113)
