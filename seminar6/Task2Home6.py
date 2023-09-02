# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.
import random


def is_safe(col, queens):
    row = len(queens)
    for queen_row, queen_col in enumerate(queens):
        if queen_col == col or \
           queen_col - queen_row == col - row or \
           queen_col + queen_row == col + row:
           return False
    return True
def check_queens_positions(queens_pos):
    queens = [pos[1] - 1 for pos in queens_pos]  # извлекаем колонны из пар и уменьшаем на 1, чтобы соответствовать индексации Python
    for row, col in enumerate(queens):
        if not is_safe(col, queens[:row]):  # проверяем безопасность для каждой строки до текущей
            return False
    return True

pos_queen = [(1,5), (2,2), (3,4), (4,7), (5,3), (6,8), (7,6), (8,1)]
print(check_queens_positions(pos_queen))

def random_pos():
    queens = []
    for row in range(8):
        cols = list(range(8))
        random.shuffle(cols)
        for col in cols:
            if is_safe(col, queens):
                queens.append(col)
                break
    return [(row + 1, col + 1) for row, col in enumerate(queens)]


successful_layouts = 0
while successful_layouts < 4:
    queens_pos = random_pos()
    if len(queens_pos) == 8:
        successful_layouts += 1
        print("Успешная расстановка:", ', '.join([f'({queen[0]},{queen[1]})' for queen in queens_pos]))





