from random import randint
def list_gen(min_elem =-10,max_elem =10, len_arr=10):
    return [randint(min_elem,max_elem) for i in range(len_arr)]

lst = list_gen()
print(lst)

def heapify(my_list, i,  n):
#левый ребёнок
    left = i * 2 + 1
#правый ребёнок
    right = i * 2 + 2
#Инициализируем наибольший элемент как корень
    largest = i
#Проверка чтоб дети не стали больше чем родители
#Если левый дочерний элемент больше корня
    if((left < n) and (my_list[left] > my_list[largest])):
        largest = left
#Если правый дочерний элемент больше,
# чем самый большой элемент на данный момент
    if((right < n) and (my_list[right] > my_list[largest])):
        largest = right;
#Если, ребёнок оказался больше родителя, то делаем обмен,
#ребёнка с родителем. Если самый большой элемент не корень
    if (i != largest):
        temp = my_list[i]
        my_list[i] = my_list[largest]
        my_list[largest] = temp
#Проверяем ещё раз чтоб дети были меньше чем родители,
#если, вдруг у детей есть свои дети
#Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        heapify(my_list, largest, n)


def heapSort(my_list):
#длина массива
    n = len(my_list)
#создаём дерево, построение кучи (перегруппируем массив)
    for i in range(n // 2 - 1,-1, -1):
        heapify(my_list, i, n)
#Делаем сортировку массива, уже отсортированного дерева,
#Один за другим извлекаем элементы из кучи
    for i in range(n-1,-1,-1):
#Перемещаем текущий корень в конец
        temp = my_list[i]
        my_list[i] = my_list[0]
        my_list[0] = temp

#Вызываем процедуру heapify на уменьшенной куче
        heapify(my_list, 0, i)


heapSort(lst);

print(lst)
