# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

def transpose(matrix):
    res = [[] for i in range(len(matrix[0]))]
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            res[i].append(matrix[j][i])
    return res


matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9] ]
transposed_matrix = transpose(matrix)
print(transposed_matrix)