class Matrix:
    '''Class simple matrix'''

    def __init__(self, data):
        """Init matrix"""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        """string representation of matrix"""

        return '\n'.join(['\t'.join([str(item) for item in row]) for row in self.data])

    def __eq__(self, other):
        """check matrix is equal"""
        return self.data == other.data

    def __add__(self, other):
        """add matrix"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrixes have different sizes!")
        result = []
        for i in range(self.rows):
            new_row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(new_row)
        return Matrix(result)

    def __mul__(self, other):
        """Multiply matrixes"""

        if self.cols != other.rows:
            raise ValueError("Количество столбцов матрицы должно быть равно количеству строк второй матрицы")
        result = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                value = sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)])
                new_row.append(value)
            result.append(new_row)
        return Matrix(result)


matrix1 = Matrix(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
matrix2 = Matrix(([7, 8, 9], [10, 11, 12], [13, 14, 15]))

print('Matrix 1:')
print(matrix1)
print('\nMatrix 2:')
print(matrix2)
print("\nСумма матриц равна: ")
print(matrix1 + matrix2)
print("\nПроизведение матриц равна: ")
print(matrix1 * matrix2)
