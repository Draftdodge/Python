#
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1.txt до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.


# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
#
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.


# queens = [(1.txt, 1.txt), (2.rrr, 3.txt), (3.txt, 5), (4, 7), (5, 2.rrr), (6, 4), (7, 6), (8, 8)]
import random
import time

NUMBER_OF_FERZE = 8
NUMBER_BOARD = 1

def generate_boards() -> list:
    list_temp = list()
    count = 1
    while count != NUMBER_OF_FERZE:
        temp = (random.randint(1, count), random.randint(1, 8))
        if temp not in list_temp:
            list_temp.append(temp)
            if not check_queens(list_temp):
                list_temp.pop()
            else:
                count +=1
    return list_temp


def is_attacking(q1: int(2), q2: int(2)) -> bool:
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    return False


def check_queens(queens: []) -> bool:
    for i in range(0, len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]): return False
    return True

s=time.time()
board_list = []
while len(board_list) < NUMBER_BOARD:
        board_list.append(generate_boards())

print(board_list)
print(time.time()-s)