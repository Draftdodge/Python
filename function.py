def show_data() -> None:
    """Выводит информацию из справочника"""
    with open("1.txt", "r", encoding="utf-8") as f:
        book = f.read()
    book = book.split('\n')
    for i, value in enumerate(book):
        print(f"№ {i+1} ->", value)

def add_data() -> None:
    # "add information"
    with open("1.txt", "a", encoding="utf-8") as f:
        fio = input("Введите ФИО: ")
        tel = input("Введите телефон: ")
        f.write(f'\n{fio} | {tel}')
    print(f"Добавлена запись: {fio} | {tel}")

def find_data() -> None:
    """поиск данных"""
    f_date =input("Введите данные для поиска: ")
    with open("1.txt", "r", encoding="utf-8") as f:
        base = f.read()
    book = base.split('\n')
    print("Результаты поиска: ")
    print(search(book, f_date))
    return

def remove_data() ->None:
    """Удаление записей"""
    with open("1.txt", "r", encoding="utf-8") as f:
        base = f.read()
    book = base.split('\n')
    print('1 - Удалить по номеру записи, 2 - Найти и удалить по ФИО или номеру')
    select = int(input())
    if select == 1:
        print_base(book)
        rem = int(input("Введите номер записи, которую следует удалить: "))
        if (rem<= len(book))and(rem > 0):
            book.pop(rem-1)
            rewrite_file(book)
        else:
            print("С указанными данными записей не найдено.")
    elif select == 2:
        f_date = input("Введите данные для поиска: ")
        num_del = search(book, f_date, 1)
        if len(num_del) == 0:
            print("С указанными данными записей не найдено.")
        else:
            print_base(book, num_del)
            rem = int(input("Введите номер записи, которую следует удалить: "))
            book.pop(rem - 1)
    else:
        print("Введены некорректные данные.")

def edit_data() ->None:
    """Редактирование записей"""
    with open("1.txt", "r", encoding="utf-8") as f:
        base = f.read()
    book = base.split('\n')
    print_base(book)
    edit_ = int(input("Введите номер записи, которую хотите отредактировать: "))
    fio = input("Введите ФИО: ")
    tel = input("Введите телефон: ")
    book[edit_-1] = (f'{fio} | {tel}')
    rewrite_file(book)

def print_base(book: list, num = []):
    for i in range(len(book)):
        if (len(num) != 0)and(i in num):
            print(f"№ {i + 1} -> {book[i]}")
        elif len(num) == 0:
            print(f"№ {i + 1} -> {book[i]}")

def rewrite_file(base: list):
    with open("1.txt", "w", encoding="utf-8") as f:
        for i in range(len(base)):
            if i < len(base) - 1:
                f.write(f'{base[i]}\n')
            else:
                f.write(f'{base[i]}')

def search(book: list, find_data: str, del_ = 0) -> str:
    """Находит в строке необходимы записи"""
    number_post = []
    if del_ == 0:
        return '\n'.join([post for post in book if find_data in post])
    else:
        for i in range(len(book)):
            if find_data in book[i]:
                number_post.append(i)
                print(number_post)
        return number_post
