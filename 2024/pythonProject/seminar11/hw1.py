import time


class MyStr(str):
    def __new__(cls, value: str, author: str = None):
        '''Value = , name = '''
        instance = super().__new__(cls, value)
        instance.author = author
        named_tuple = time.localtime()  # получить struct_time
        instance.time = time.strftime("%Y-%m-%d %H:%M", named_tuple)
        return instance
    def __init__(self, value: str, author: str = None):
        self.value = value
        self.author = author



    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'
    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"

if __name__ == '__main__':
    event = MyStr("Завершилось тестирование", "John")
    print(event)
    my_string = MyStr("Пример текста", "Иван")
    print(my_string)
    my_string = MyStr("Мама мыла раму", "Маршак")
    print(repr(my_string))