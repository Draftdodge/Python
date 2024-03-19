import csv


class NameError_(ValueError):
    pass


class Control_name():
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, name):
        fullname = name.split(' ')
        for i in fullname:
            if not i.isalpha() or not i[0].istitle():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        setattr(instance, self.name, name)


class CsvData:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        with open(getattr(instance, self.name), 'r', encoding='UTF-8') as f:
            res = {}
            for i in [*csv.reader(f)][0]:
                res.setdefault(i, ([], []))
            print(res)
            return res

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.split('.')[-1] == 'csv':
            raise ValueError('Файл не найден')
        else:
            setattr(instance, self.name, value)


class Student():
    _full_name = Control_name()
    _subjects = CsvData()

    def __init__(self, name, csv_file):
        self._full_name = name
        self._subjects = csv_file
        self.grades = self._subjects.copy()

    def add_grade(self, subject, mark):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(mark, int) or not 2 <= mark <= 5:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            self.grades[subject][0].append(mark)

    def add_test_score(self, subject, test_score):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            raise ValueError(f'Оценка должна быть целым числом от 0 до 100')
        else:
            self.grades[subject][1].append(test_score)

    def get_average_grade(self):
        all_grades = [*filter(lambda x: x.isdigit(),
                              str([m for s, (m, t)
                                   in self.grades.items() if m or t]))]
        return sum(map(int, all_grades)) / len(all_grades)

    def get_average_test_score(self, subject):
        if subject not in self.grades:
            raise ValueError(f'Предмет {subject} не найден')
        all_test_scores = [[n for s, (m, t) in self.grades.items()
                            for n in t if s == subject]]
        return sum(*all_test_scores) / len(all_test_scores)

    def __str__(self):
        return f'Студент: {self._full_name}\n' \
               f'Предметы: ' \
               f'{", ".join([s for s, (m, t) in self.grades.items() if m or t])}'


# class Student():
#     full_name = Control_name()
#     subjects = CsvData()
#     def __init__(self, name, file_name):
#         self.subjects = dict()
#         self.name = Control_name(self.name)
#         with open(file_name, "r", encoding='utf-8') as f:
#             data = csv.reader(f, delimiter=",")
#             for i in next(data):
#                 self.subjects[i] = {'test':[], 'grade':[]}

if __name__ == '__main__':
    student = Student('Dfdtk Fylhttdbx Dybyty', 'subjects.csv')
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    student.add_grade("Литература", 5)
    student.add_test_score("Литература", 90)
    student.add_test_score("Литература", 50)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Литература")
    print(f"Средний результат по тестам по Литература: {average_test_score}")

    print(student)