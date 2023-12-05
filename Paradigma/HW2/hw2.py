def table_multiplication(number):
    for i in range(1, number + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print('')


if __name__ == '__main__':
    num = int(input("Введите число n: "))
    table_multiplication(num)


# В данном примере выбрана процедурная парадигма, так как она является
# простой и понятной для решения этой задачи.