# Создайте функцию, которая удаляет из текста
# все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from string import ascii_letters
import unittest

class TestClearText(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(clear_text('hello world'), 'hello world', msg='строка изменена')
    def test_register(self):
        self.assertEqual(clear_text('Hello world'), 'hello world')
    def test_delete_punctuation(self):
        self.assertEqual(clear_text('Hello world!'), 'hello world')
    def test_delete_latter_oun_lang(self):
        self.assertEqual(clear_text('Hello мир'), 'hello ')
    def test_correct_all(self):
        self.assertEqual(clear_text('Hello world, мир!!!'), 'hello world ')
def clear_text(s: str) ->str:
    chars = ascii_letters + ' '
    return ''.join([c for c in s if c in chars]).lower()


if __name__ == '__main__':
    unittest.main(verbosity=5)
    # print(clear_text('Hello world!'))
