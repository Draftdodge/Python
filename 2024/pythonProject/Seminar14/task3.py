# Создайте функцию, которая удаляет из текста
# все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from string import ascii_letters
import pytest


def test_no_changes():
    assert clear_text('hello world') == 'hello world', "Error"
def test_register():
    assert clear_text('Hello world') == 'hello world', "Error"
def test_delete_punctuation():
    assert clear_text('Hello world!!!') == 'hello world', "Error"
def test_delete_latter_oun_lang():
    assert clear_text('Hello мир') == 'hello ', "Error"
def test_correct_all():
    assert clear_text('Hello world, мир!!!') == 'hello world ', "Error"
def clear_text(s: str) ->str:
    chars = ascii_letters + ' '
    return ''.join([c for c in s if c in chars]).lower()


if __name__ == '__main__':
    pytest.main()
    # print(clear_text('Hello world!'))
