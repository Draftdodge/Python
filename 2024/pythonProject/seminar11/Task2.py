class Singleton:
    _instance = None
    def __new__(cls, text, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.oldtext = []
            cls._instance.oldname = []
        else:
            cls._instance.oldtext.append(cls._instance.text)
            cls._instance.oldname.append(cls._instance.name)
        return cls._instance
    def __init__(self, text, name):
        self.text = text
        self.name = name
    # def __init__(self, name: str):
    #     self.name = name
    #     a = Singleton('Первый')
    #     print(f'{a.name = }')
    #     b = Singleton('Второй')
    #     print(f'{a is b = }')
    #     print(f'{a.name = }\n{b.name = }')

if __name__ == '__main__':
    a = Singleton('1', '1')
    b = Singleton('2', '2')
    c = Singleton('3', '3')
    d = Singleton('4', '4')
    print(c)
    print(b)
    print(c.oldtext)
    print(c.oldname)
    print(c.text)
    print(c.name)