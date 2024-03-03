import csv
import logging

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(format=FORMAT, filename='Student.log', filemode='w', encoding='utf-8', style='{',
                    level=logging.DEBUG)


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
                logging.error('Неверное ФИО. Должно состоять только из букв и начинаться с заглавной буквы')
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
            return res

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.split('.')[-1] == 'csv':
            logging.error(f"Файл с именем {value} не найден")
            raise ValueError('Файл не найден')
        else:
            setattr(instance, self.name, value)


class Student():
    full_name = Control_name()
    subjects = CsvData()

    def __init__(self, name, csv_file):
        self.full_name = name
        self.subjects = csv_file
        self.grades = self.subjects.copy()
        logging.debug(f'Создан профиль студента {self.full_name}')

    def add_grade(self, subject, mark):
        if subject not in self.grades:
            logging.error(f'Предмет {subject} не найден')
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(mark, int) or not 2 <= mark <= 5:
            logging.error('Оценка должна быть целым числом от 2 до 5')
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            self.grades[subject][0].append(mark)
            logging.debug(f'Добавлена оценка по предмету {subject}: {self.grades[subject][0]}')

    def add_test_score(self, subject, test_score):
        if subject not in self.grades:
            logging.error(f'Предмет {subject} не найден')
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            logging.error('Оценка должна быть целым числом от 0 до 100')
            raise ValueError('Оценка должна быть целым числом от 0 до 100')
        else:
            self.grades[subject][1].append(test_score)
            logging.debug(f'Добавлена оценка (баллы) по тестам по предмету {subject}: {self.grades[subject][1]}')

    def get_average_grade(self):
        all_grades = [*filter(lambda x: x.isdigit(),
                              str([m for s, (m, t)
                                   in self.grades.items() if m or t]))]
        res = sum(map(int, all_grades)) / len(all_grades)
        logging.debug(f'Средняя оценка по всем дисциплинам: {res}')
        return res

    def get_average_test_score(self, subject):
        if subject not in self.grades:
            logging.error(f'Предмет {subject} не найден')
            raise ValueError(f'Предмет {subject} не найден')
        all_test_scores = [n for s, (m, t) in self.grades.items() for n in t if s == subject]
        res = sum(all_test_scores) / len(all_test_scores)
        logging.debug(f'Средний балл по тестам по предмету {subject}: {res}')
        return res

    def __str__(self):
        return f'Студент: {self.full_name}\n' \
               f'Предметы: ' \
               f'{", ".join([s for s, (m, t) in self.grades.items() if m or t])}'


if __name__ == '__main__':
    student = Student('Dfdtk Fylhttdbx Dybyty', 'subjects.csv')
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    student.add_grade("Литература", 5)
    student.add_test_score("Литература", 90)
    student.add_test_score("Литература", 50)
    student.add_test_score("Литература", 40)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Литература")
    print(f"Средний результат по тестам по Литература: {average_test_score}")

    print(student)
