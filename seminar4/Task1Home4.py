# Напишите функцию для транспонирования матрицы
def transpose(matrix):
    if not matrix:             #Проверка на пустую матриц
        return []

    row_lenght = len(matrix[0])

    for row in matrix:                     #Проверка длины строк матрицы
        if len(row) != row_lenght:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])
        transposed.append(transposed_row)
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
try:
    transposed_matrix = transpose(matrix)
    for row in transposed_matrix:
        print(row)
except ValueError as e:
    print(e)
