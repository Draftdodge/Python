import pytest
from HW import Student, Control_name, CsvData

def test_fullname():
    student1 = Student('Ivanov Ivan Ivanovich', 'subjects.csv')
    assert (student1.full_name) == 'Ivanov Ivan Ivanovich'
def test_load_subjects():
    student1 = Student('Ivanov Ivan Ivanovich', 'test.csv')
    print(student1.subjects)
    assert (student1.subjects) == {'История': ([], []), 'Математика': ([], []), 'Физика': ([], [])}

def test_average_grade():
    student1 = Student('Ivanov Ivan Ivanovich', 'test.csv')
    student1.add_grade("Математика", 4)
    student1.add_grade("Физика", 3)
    student1.add_grade("История", 2)
    assert (student1.get_average_grade()) == 3

def test_uncorrect_grade():
    student1 = Student('Ivanov Ivan Ivanovich', 'test.csv')
    with pytest.raises(ValueError):
        student1.add_grade("Математика", 7)

def test_average_test_score():
    student1 = Student('Ivanov Ivan Ivanovich', 'test.csv')
    student1.add_test_score("История", 50)
    student1.add_test_score("История", 100)
    student1.add_test_score("Физика", 30)
    assert (student1.get_average_test_score('История')) == 75

def test_uncorrect_test_score():
    student1 = Student('Ivanov Ivan Ivanovich', 'test.csv')
    with pytest.raises(ValueError):
        student1.add_test_score("Математика", 'сто')

if __name__ == '__main__':
    pytest.main()