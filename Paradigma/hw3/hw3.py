import random
class game_XO:
    # Задаем таблицу сетки
    table = list(range(1, 10))
    opponent = 0

    # Выбор второго игрока или компьютер
    def choosing_an_opponent(self):
        print("С кем хотите поиграть?")
        print("Если с человеком, то введите --- 0 ---")
        print("Если с компьютером, то введите --- 1 ---")
        valid = False
        while not valid:
            self.opponent = int(input("Введите ваш выбор: "))
            if (self.opponent == 0):
                print("Итак, вы выбрали человека.")
                valid = True
            elif (self.opponent == 1):
                print("Итак, вы выбрали компьютер.")
                valid = True
            else:
                print("Некорректный ввод!")


    # Рисуем таблицу сетки
    def table_grid(self):
        for i in range(3):
            print("|", self.table[0 + i * 3], "|", self.table[1 + i * 3], "|", self.table[2 + i * 3], "|")

    # Ходим
    def make_move(self, step):
        valid = False
        while not valid:
            value = int(input("Введите номер клетки куда поставить " + step + "? "))
            if 1 <= value <= 9:
                if (str(self.table[value - 1]) != "X") & (str(self.table[value - 1]) != "O"):
                    self.table[value - 1] = step
                    valid = True
                else:
                    print("Эта клетка занята")
            else:
                print("Некорректный ввод!")

    def ii_move(self):
        valid = False
        while not valid:
            value = random.randint(1, 9)
            print(value)
            if (str(self.table[value - 1]) != "X") & (str(self.table[value - 1]) != "O"):
                self.table[value - 1] = "O"
                valid = True

    # Условия победы
    def winner(self):
        win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for x in win:
            if self.table[x[0]] == self.table[x[1]] == self.table[x[2]]:
                return self.table[x[0]]
        return False

    # Запуск игры
    def play(self):
        count = 0
        win = False
        game_XO.choosing_an_opponent(self)
        while not win:
            game_XO.table_grid(self)
            if count % 2 == 0:
                game_XO.make_move(self, "X")
            else:
                if self.opponent == 1:
                    print("Ход компьютера: ")
                    game_XO.ii_move(self)
                else:
                    game_XO.make_move(self, "O")
            count += 1
            if count > 4:
                m = game_XO.winner(self)
                if m:
                    print("--- ", m, " --- Победил!")
                    win = True
                    break
            if count == 9:
                print("Ничья!")
                break
        game_XO.table_grid(self)
