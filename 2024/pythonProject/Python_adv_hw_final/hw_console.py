from HW import Student
import argparse

def cl_parser():
    parser = argparse.ArgumentParser(description='Создание профиля студента')
    parser.add_argument('-f', '--filename', default='test.csv')
    parser.add_argument('-n', '--name', default='Иванов Иван Иванович')
    args = parser.parse_args()
    return Student(args.name, args.filename)

if __name__ == '__main__':
    student = cl_parser()
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