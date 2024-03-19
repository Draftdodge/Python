class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data == None:
            self.data = []
        else:
            self.data = data
        for i in range(0, self.rows):
            self.data.append([])
            for j in range(0, self.cols):
                self.data[i].append(0)
        # print(self.data)

    def __str__(self):
        matrix = ''
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if j!= self.cols-1:
                    matrix += f'{self.data[i][j]} '
                else:
                    matrix += f'{self.data[i][j]}'
            if i != self.rows -1:
                matrix += f'\n'
        return matrix

    def __eq__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            if self.data == other.data:
                return True
        return False

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = []
            for i in range(0, self.rows):
                new_matrix.append([])
                for j in range(0, self.cols):
                    new_matrix[i].append(self.data[i][j] + other.data[i][j])
            return Matrix(self.rows, self.cols, new_matrix)
        return f'Матрицы имеют различный размер, сложение невозможно.'

    def __mul__(self, other):
        if self.cols == other.rows:
            new_matrix = list(
                map(lambda x: list(map(lambda y: sum(i * j for i, j in zip(x, y)), zip(*other.data))), self.data))
            return Matrix(self.rows, self.cols, new_matrix)
        return f'Умножение матриц невозможно.'


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

print(matrix1 == matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
