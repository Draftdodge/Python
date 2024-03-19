import time


class MyString(str):
    def __new__(cls, value: str, name: str = None):
        '''Value = , name = '''
        instance = super().__new__(cls, value)
        instance.name = name
        time.sleep(1)
        instance.time = time.ctime()
        return instance


if __name__ == '__main__':
    t = MyString("Hello, 1 string", "alex")
    t2 = MyString("Hello, 2 string", "Joe")
    t3 = MyString("Hello, 3 string")
    st = t + t2 + t3 + 'Hello'
    print(f'{st = }')
    print(f'{t = }\t{t.name = }\t{t.time = }')
    print(f'{t2 = }\t{t2.name = }\t{t2.time = }')
    print(f'{t3 = }\t{t3.name = }\t{t3.time = }')
