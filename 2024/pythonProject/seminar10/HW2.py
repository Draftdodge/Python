# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
#
# Напишите класс LotteryGame, который будет иметь метод compare_lists,
# который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2
#
# Если совпадающих чисел нет, то выведите на экран:
# Совпадающих чисел нет.


class LotteryGame:
    def __init__(self, ticket: list, win_numbers: list):
        self.ticket = ticket
        self.win_numbers = win_numbers

    def compare_lists(self) -> list:
        res = []
        for i in self.ticket:
            if i in self.win_numbers:
                res.append(i)
        if len(res) !=0:
            print(f'Совпадающие числа: {res}')
            print(f'Количество совпадающих чисел: {len(res)}')
        else:
            print('Совпадающих чисел нет.')




list1 = []
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
print(f'Совпадающие числа: {matching_numbers}')
print(f'Количество совпадающих чисел: {len(matching_numbers)}')
